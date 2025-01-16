from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from sqlalchemy.orm import Session
from models import UserQuestion
from schemas import QuestionRequest, Answer
from fastapi import HTTPException
import logging
import re


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Use bigger models depending on hardware configuration
MODEL_NAME = "EleutherAI/gpt-neo-1.3B" 
logger.info(f"Loading model: {MODEL_NAME}")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# LLM initialization for the generation of text
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0) # change this if using CPU

def clean_generated_text(text: str) -> str:
    """Clean and format the generated text."""
    # Remove unwanted artifacts
    text = re.sub(r"(Please generate|Focus on the topic|In this case|Ensure the output)", "", text)
    
    return " ".join(text.split()) # to remove extra whitespaces

def extract_sections(raw_output: str) -> tuple:

    main_question_match = re.search(r"Main Question:\s*(.*?)\n", raw_output, re.DOTALL)
    related_qas_match = re.search(r"Related Questions and Answers:\s*(.*)", raw_output, re.DOTALL)

    main_question = main_question_match.group(1).strip() if main_question_match else "No main question provided."
    related_qas = related_qas_match.group(1).strip() if related_qas_match else "No related Q&A provided."
    
    return main_question, related_qas

"""To filter repetitive content"""
def filter_repetitive_sentences(text: str, max_sentences: int) -> str:

    sentences = text.split(". ")
    seen_sentences = set()
    filtered_sentences = []

    for sentence in sentences:
        cleaned_sentence = sentence.strip()
        if cleaned_sentence and cleaned_sentence not in seen_sentences:
            filtered_sentences.append(cleaned_sentence)
            seen_sentences.add(cleaned_sentence)
        if len(filtered_sentences) >= max_sentences:
            break

    return ". ".join(filtered_sentences) + ('.' if filtered_sentences else '')

def generate_questions(request: QuestionRequest, db: Session) -> Answer:

    prompt = (
        f"Generate a specific interview question for the role of {request.role}.\n"
        f"Focus on the topic: {request.user_input}.\n"
        f"Provide additional 2-3 related questions with answers, keeping responses concise.\n\n"
        f"Main Question:\n"
        f"Related Questions and Answers:\n"
    )

    try:
        # Generation of text using the above model
        response = generator(
            prompt,
            max_length=500,
            num_return_sequences=1,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            repetition_penalty=1.5
        )
        raw_output = response[0]["generated_text"]
        logger.info(f"Generated raw output: {raw_output}")


        main_question, related_qas = extract_sections(raw_output)

        main_question = clean_generated_text(main_question)
        related_qas = clean_generated_text(related_qas)
        main_question = filter_repetitive_sentences(main_question, max_sentences=2)
        related_qas = filter_repetitive_sentences(related_qas, max_sentences=5)

        # Save to database
        db_entry = UserQuestion(
            role=request.role,
            question=main_question,
            answer=related_qas,
        )
        db.add(db_entry)
        db.commit()
        db.refresh(db_entry)

        # Return the response
        return Answer(role=request.role, question=main_question, answer=related_qas)

    except Exception as e:
        logger.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
