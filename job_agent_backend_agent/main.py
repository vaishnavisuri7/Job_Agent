from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import crud, models, schemas

from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:4200",  # Frontend URL
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate/", response_model=schemas.Answer)
def generate_response(request: schemas.QuestionRequest, db: Session = Depends(get_db)):

    if not request.role or not request.user_input:
        raise HTTPException(status_code=400, detail="Role and user input cannot be empty.")

    response = crud.generate_questions(request, db)
    if not response:
        raise HTTPException(status_code=500, detail="Failed to generate response.")
    return response
