from fastapi import FastAPI
from app.src.admin.router import admin
from app.src.guest.router import guest
import consul
import os
import socket
import logging

app = FastAPI(title="Restaurant order taker")

app.include_router(admin, tags=["admin"])
app.include_router(guest, tags=["guest"])


@app.on_event("startup")
async def startup_event():
    c = consul.Consul(
        host=os.getenv("CONSUL_HOST", "consul"),
        port=int(os.getenv("CONSUL_PORT", "8500")),
    )

    service_name = "app"
    service_port = int(os.getenv("APP_SERVICE_INTERNAL_PORT", "80"))
    service_id = f"{service_name}-{socket.gethostname()}"

    c.agent.service.register(
        name=service_name,
        service_id=service_id,
        address=socket.gethostbyname(socket.gethostname()),
        port=service_port,
        check={
            "http": f"http://{socket.gethostname()}:{service_port}/health",
            "interval": "10s",
            "DeregisterCriticalServiceAfter": "10s",
        },
    )

    logging.info(f"{service_name} service registered with Consul")

@app.get("/", tags=["main page"])
async def root():
    return "Restaurant order taker"

@app.get("/health")
def health_check():
    return {"status": "healthy"}