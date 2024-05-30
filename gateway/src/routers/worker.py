from fastapi import APIRouter
from gateway.src.utils import get_service_url
import httpx
worker = APIRouter(prefix="/worker")

@worker.post("/deque_request")
async def deque_request():
    url = get_service_url("worker") + "/deque_request"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()