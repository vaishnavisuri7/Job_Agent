from sqlalchemy import Column, Integer, String, Text
from database import Base

class UserQuestion(Base):
    __tablename__ = "user_questions"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, index=True, nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
