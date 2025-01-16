# Job Interview Preparation Agent

## 🚀 Introduction
Navigating the job market as an active job seeker has been quite challenging, particularly when it comes to interview preparation. This led me to develop a **Job Interview Preparation Agent**. This tool aims to assist users by offering personalized interview questions, answers, and tips tailored to their specific job roles or topics. Although still evolving, this project is a step towards making interview prep more accessible and effective.

## 🛠️ Technologies Used
- **Backend**: Utilizing **FastAPI** for a swift and straightforward backend that manages user inputs and orchestrates the agent's operations.
- **Control Flow**: Currently, **GPT-Neo from Hugging Face** is employed for managing the control flow and generating responses. However, the system is designed to be flexible; other LLM models can also be substituted. If we have access to other APIs, they can be easily swapped in to potentially enhance response quality.
- **Frontend**: The frontend is built using **Angular CLI**, designed to offer a simple and intuitive user interface.

## 🌱 Why This Project?
This project resonates with my current situation as someone in the job market. I sought to create a tool that would facilitate organized and effective interview preparation. While the initial version has room for improvement, it lays down a solid foundation for further development, aiming to deliver valuable insights, questions, and tips for interviewees.

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

