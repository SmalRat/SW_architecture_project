from fastapi import APIRouter
from gateway.src.utils import get_service_url
import httpx
import logging
support = APIRouter(prefix="/support")


@support.post("/create_session")
async def create_session():
    url = get_service_url("support") + "/create_session"

    async with httpx.AsyncClient() as client:
        logging.info(f"Request url: {url}")
        response = await client.post(url, timeout=10)
        return response.json()

@support.post("/put_message_user")
async def put_message_user(session_id: int, message: str):
    url = get_service_url("support") + f"/put_message_user?session_id={session_id}&message={message}"
    async with httpx.AsyncClient() as client:
        response = await client.post(url)
        return response.json()

@support.post("/put_message_admin")
async def put_message_admin(session_id: int, message: str):
    url = get_service_url("support") + f"/put_message_admin?session_id={session_id}&message={message}"
    async with httpx.AsyncClient() as client:
        response = await client.post(url)
        return response.json()

@support.get("/get_session")
async def get_session(session_id: int):
    url = get_service_url("support") + f"/get_session?session_id={session_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()