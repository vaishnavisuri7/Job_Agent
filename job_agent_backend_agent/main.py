from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import crud, models, schemas

from fastapi.middleware.cors import CORSMiddleware

# Allowed origins for CORS
origins = [
    "http://localhost:4200",  # Frontend URL
]

# Initialize FastAPI app
app = FastAPI()

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate/", response_model=schemas.Answer)
def generate_response(request: schemas.QuestionRequest, db: Session = Depends(get_db)):
    """Endpoint to generate interview questions and answers."""
    if not request.role or not request.user_input:
        raise HTTPException(status_code=400, detail="Role and user input cannot be empty.")

    response = crud.generate_questions(request, db)
    if not response:
        raise HTTPException(status_code=500, detail="Failed to generate response.")
    return response
