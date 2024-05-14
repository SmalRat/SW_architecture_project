from fastapi import FastAPI, HTTPException
import httpx
import consul
import random

app = FastAPI()
c = consul.Consul()

def get_service_url(service_name: str) -> str:
    index, services = c.health.service(service_name, passing=True)
    print(services)
    if not services:
        raise HTTPException(status_code=404, detail=f"Service {service_name} not found")
    random_service = random.choice(services)
    print(random_service)
    return f"http://{random_service['ServiceAddress']}:{random_service['ServicePort']}"

@app.post("/deque_request")
async def deque_request():
    url = get_service_url("support-worker-service") + "/deque_request"
    async with httpx.AsyncClient() as client:
        response = await client.post(url)
        return response.json()

@app.post("/create_session")
async def create_session():
    url = get_service_url("support-service") + "/create_session"
    async with httpx.AsyncClient() as client:
        response = await client.post(url)
        return response.json()

@app.post("/put_message_user")
async def put_message_user():
    url = get_service_url("support-service") + "/put_message_user"
    async with httpx.AsyncClient() as client:
        response = await client.post(url)
        return response.json()

@app.post("/put_message_admin")
async def put_message_admin():
    url = get_service_url("support-service") + "/put_message_admin"
    async with httpx.AsyncClient() as client:
        response = await client.post(url)
        return response.json()

@app.get("/get_session")
async def get_session():
    url = get_service_url("support-service") + "/get_session"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()