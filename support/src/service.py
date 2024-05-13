from typing import List

from fastapi import APIRouter

from support.src.utils import SupportRepository, client

repo = SupportRepository()

class SupportService:
    def __init__(self):
        mq_name = "mq"
        self.messaging_queue = client.get_queue(mq_name).blocking()

    def create_session(self):
        return repo.create_session()

    def put_message_user(self, session_id, message):
        self.messaging_queue.put(session_id)
        return repo.put_message(session_id, "User", message)

    def put_message_admin(self, session_id, message):
        return repo.put_message(session_id, "Admin", message)

    def get_session(self, session_id):
        return self.messaging_queue.take() #repo.get_session(session_id)