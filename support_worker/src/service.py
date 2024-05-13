from typing import List

from fastapi import APIRouter

from support.src.utils import SupportRepository
import support.src.common

repo = SupportRepository()

class SupportService:
    @staticmethod
    def create_session():
        return repo.create_session()

    @staticmethod
    def put_message_user(session_id, message):
        return repo.put_message(session_id, "User", message)

    @staticmethod
    def put_message_admin(session_id, message):
        return repo.put_message(session_id, "Admin", message)

    @staticmethod
    def get_session(session_id):
        return repo.get_session(session_id)