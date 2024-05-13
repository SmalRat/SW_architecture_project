from typing import List
from fastapi import FastAPI
from fastapi import APIRouter

from support.src.service import SupportService

SUPPORT_SERVICE_CREATE_SESSION_ENDPOINT = "/create_session"
SUPPORT_SERVICE_PUT_MESSAGE_USER_ENDPOINT = "/put_message_user"
SUPPORT_SERVICE_PUT_MESSAGE_ADMIN_ENDPOINT = "/put_message_admin"
SUPPORT_SERVICE_GET_SESSION_ENDPOINT = "/get_session"
SUPPORT_SERVICE_HOSTNAME = "localhost"


app = FastAPI(title="Support")

@app.get("/", tags=["main page"])
async def root():
    return "Support"


@app.post(SUPPORT_SERVICE_CREATE_SESSION_ENDPOINT)
def create_session():
    SupportService.create_session()


@app.post(SUPPORT_SERVICE_PUT_MESSAGE_USER_ENDPOINT)
def put_message_user(session_id: int, message: str):
    SupportService.put_message_user(session_id, message)


@app.post(SUPPORT_SERVICE_PUT_MESSAGE_ADMIN_ENDPOINT)
def put_message_admin(session_id: int, message: str):
    SupportService.put_message_admin(session_id, message)


@app.get(SUPPORT_SERVICE_GET_SESSION_ENDPOINT)
def get_session(session_id: int):
    SupportService.get_session(session_id)

