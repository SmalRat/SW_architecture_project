from fastapi import APIRouter
from gateway.src.utils import get_service_url
import httpx
from gateway.src.routers.models import *
booking = APIRouter(prefix="/booking")

# Routes
@booking.post("/create_booking/")
async def create_booking(booking: Booking):
    url = get_service_url("booking") + "/create_booking/"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=booking.json())
        return response.json()


@booking.get("/bookings/{user_name}")
async def get_user_bookings(user_name: str):
    url = get_service_url("booking") + f"/bookings/{user_name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@booking.get("/bookings/")
async def get_all_bookings():
    url = get_service_url("booking") + f"/bookings/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@booking.get("/tables/")
async def get_all_tables():
    url = get_service_url("booking") + f"/tables/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@booking.get("/tables/{table}")
async def get_table(table: int):
    url = get_service_url("booking") + f"/tables/{table}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()