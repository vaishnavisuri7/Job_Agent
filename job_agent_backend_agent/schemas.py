from pydantic import BaseModel

class QuestionRequest(BaseModel):
    role: str
    user_input: str

class Answer(BaseModel):
    role: str
    question: str
    answer: str

    class Config:
        orm_mode = True
