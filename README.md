# portofolio_chatbot

🧠 Backend (Chatbot)

An AI-powered assistant that helps users navigate the portfolio and answers questions about projects, skills, and experience. Built with FastAPI and integrated with the Google Gemini API.

    Tech Stack: FastAPI, Python, Gemini API

    Features:

        Natural language chatbot

        Context-aware responses from portfolio content

    Deployment: Render

🔗 **Live Site:** [https://portfolio-chatbot-92au.onrender.com/docs/]("https://portfolio-chatbot-92au.onrender.com/docs/")


## 💻 How to Run the Project Locally

1. Open a terminal.

2. Navigate to the project folder:

    - using docker
   ```bash
   sudo docker-compose up
   ```
   vist [Docs]("http://0.0.0.0:8000/docs")

    - run it manuly
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
    vist [Docs]("http://127.0.0.1:8000/docs")
