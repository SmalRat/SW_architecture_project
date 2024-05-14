from fastapi import APIRouter

from support.src.service import SupportService

SUPPORT_SERVICE_CREATE_SESSION_ENDPOINT = "/create_session"
SUPPORT_SERVICE_PUT_MESSAGE_USER_ENDPOINT = "/put_message_user"
SUPPORT_SERVICE_PUT_MESSAGE_ADMIN_ENDPOINT = "/put_message_admin"
SUPPORT_SERVICE_GET_SESSION_ENDPOINT = "/get_session"
SUPPORT_SERVICE_HOSTNAME = "localhost"

support = APIRouter(prefix="")
svc = SupportService()


@support.get("/", tags=["main page"])
async def root():
    return "Support"


@support.post(SUPPORT_SERVICE_CREATE_SESSION_ENDPOINT)
def create_session():
    return svc.create_session()


@support.post(SUPPORT_SERVICE_PUT_MESSAGE_USER_ENDPOINT)
def put_message_user(session_id: int, message: str):
    return svc.put_message_user(session_id, message)


@support.post(SUPPORT_SERVICE_PUT_MESSAGE_ADMIN_ENDPOINT)
def put_message_admin(session_id: int, message: str):
    return svc.put_message_admin(session_id, message)


@support.get(SUPPORT_SERVICE_GET_SESSION_ENDPOINT)
def get_session(session_id: int):
    return svc.get_session(session_id)
