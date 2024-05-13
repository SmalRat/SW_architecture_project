from typing import List, Optional
from pydantic import BaseModel

# class Dialog:
#     def __init__(self, session_id):
#         self.session_id = session_id
#         self.messages = []
#
#     def get_messages(self):
#         return self.messages
#
#
# class Message:
#     def __init__(self, role, message):
#         self.sender = role
#         self.message = message
#
#     def to_string(self):
#         return self.message

class Message(BaseModel):
    sender: str
    message: str

class Dialog(BaseModel):
    session_id: int
    messages: list[Message]


