from fastapi import APIRouter, HTTPException
from gateway.src.utils import get_service_url
import httpx
from gateway.src.routers.models import *
booking = APIRouter(prefix="/booking")

# Routes
@booking.post("/create_booking/")
async def create_booking(booking: Booking):
    url = get_service_url("booking") + "/create_booking/"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, data=booking.json())
            response.raise_for_status()  # Raise exception for non-2xx status codes
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

@booking.get("/bookings/{user_name}")
async def get_user_bookings(user_name: str):
    url = get_service_url("booking") + f"/bookings/{user_name}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

@booking.get("/bookings/")
async def get_all_bookings():
    url = get_service_url("booking") + f"/bookings/"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

@booking.get("/tables/")
async def get_all_tables():
    url = get_service_url("booking") + f"/tables/"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

@booking.get("/tables/{table}")
async def get_table(table: int):
    url = get_service_url("booking") + f"/tables/{table}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()  # Raise exception for non-2xx status codes
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
