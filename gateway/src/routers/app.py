from fastapi import APIRouter
from gateway.src.routers.models import *
from gateway.src.utils import get_service_url
import httpx
app_admin = APIRouter(prefix="/app_admin")
app_user = APIRouter(prefix="/app_user")

@app_admin.get("/orders", response_model=List[Order_stats])
async def get_completed_orders_info():
    url = get_service_url("app") + "/admin/orders"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@app_admin.get("/stats", response_model=General_stats)
async def get_general_stats():
    url = get_service_url("app") + "/admin/stats"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@app_admin.post("/add_menu_item", response_model=Id)
async def add_menu_item(item: Menu_item):
    url = get_service_url("app") + "/admin/add_menu_item"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=item.json())
        return response.json()


@app_admin.put("/change_stock/{item_id}", response_model=In_stock)
async def change_stock(item_id: int, in_stock: int):
    url = get_service_url("app") + f"/admin/change_stock/{item_id}?in_stock={in_stock}"
    async with httpx.AsyncClient() as client:
        response = await client.put(url)
        return response.json()


@app_admin.get("/get_menu", response_model=list[Item])
async def get_menu():
    url = get_service_url("app") + f"/admin/get_menu"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

@app_user.get("", response_model=Message_responce)
async def root():
    url = get_service_url("app") + f"/guest"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@app_user.get("/menu", response_model=List[Menu_item_user])
async def get_menu():
    url = get_service_url("app") + f"/guest/menu"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@app_user.post("/create_session", response_model=Create_order_responce)
async def create_session():
    url = get_service_url("app") + f"/guest/create_session"
    async with httpx.AsyncClient() as client:
        response = await client.post(url)
        return response.json()


@app_user.post("/send_message/{session_id}", response_model=Message_responce)
async def handle_message(session_id: int, message: str):
    url = get_service_url("app") + f"/guest/send_message/{session_id}?message={message}"
    async with httpx.AsyncClient() as client:
        response = await client.post(url)
        return response.json()

