from pydantic import BaseModel


class Message(BaseModel):
    sender: str
    message: str


class Dialog(BaseModel):
    session_id: int
    messages: list[Message]


