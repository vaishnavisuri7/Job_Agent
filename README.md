# Job Interview Preparation Agent

## 🚀 Introduction
As a job seeker for the past few months, I found it challenging to prepare efficiently for interviews. This led me to create a simple **Job Interview Preparation Agent**. It’s a humble attempt to help users by providing tailored interview questions, answers, and tips based on their desired role or topic. While it’s still a work in progress, I aim to continue improving its functionality.

## 🛠️ Technologies Used
- **Backend**: Developed with **FastAPI**, providing a fast and simple backend for handling user inputs and managing the flow of the agent.
- **Control Flow**: **GPT-Neo** from Hugging Face is used for handling the control flow and generating responses, though the question and answer generation still requires further improvement due to resource constraints.
- **Frontend**: The frontend is built using **Angular CLI**, designed to offer a simple and intuitive user interface.

## 🌱 Why This Project?
This project is built around a topic that is highly relevant to me right now. As someone actively searching for jobs, I wanted to create a tool that can assist in preparing for interviews in an organized way. While the current version isn't perfect, it provides a foundation that can be expanded to generate useful insights, questions, and tips.

## 💡 Features
- Users can input their role and the topic they want to focus on for interview preparation.
- The **LLM** (GPT-Neo) is used to handle the flow, generating content for technical or soft skill questions based on the user’s input.
- A simple, clean **Angular** frontend displays the output to the user.

## 👨‍💻 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/vaishnavisuri7/Job_Agent.git
   ```
2. Set up the backend:

* Navigate to the backend directory and install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

* Run the FastAPI backend:
```bash
uvicorn main:app --reload
```
3. Set up the frontend:

* Navigate to the frontend directory and install dependencies:
```bash
cd frontend
npm install
```
* Run the Angular frontend:
```bash
ng serve
```
4. Open the application in your browser at http://localhost:4200.

## 🔨 Future Improvements
- Enhance the question and answer generation for more accurate and relevant interview preparation.
- Support additional domains and roles to cover a wider range of interview topics.
- Improve user interaction and UI/UX for a smoother experience.

