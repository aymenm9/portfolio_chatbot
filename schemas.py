from pydantic import BaseModel
from typing import Optional, List



class chat_turn(BaseModel):
    role:str
    text:str

class chat_history(BaseModel):
    history:Optional[List[chat_turn]]

class chat_input(BaseModel):
    role:str = 'user'
    text:str
class chat_output(BaseModel):
    role:str = 'model'
    text:str