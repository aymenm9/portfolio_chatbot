from typing import Union
from fastapi import FastAPI
from chat_bot import generate
from schemas import chat_history,chat_output, chat_input

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/v1/chat_bot")
def chat_bot(user_input:chat_input, chat_history:chat_history)->chat_output:
    chat = generate(user_input.text, chat_history)
    return chat_output(text=chat)