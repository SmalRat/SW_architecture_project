import random

from fastapi import FastAPI
from worker.src.service import SupportWorkerService
import consul
import os
import uuid
import socket

SUPPORT_WORKER_SERVICE_GET_NEW_SESSION = "/deque_request"

app = FastAPI(title="Support worker")

svc = SupportWorkerService()

@app.get("", tags=["support worker page"])
async def root():
    return "Support"


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get(SUPPORT_WORKER_SERVICE_GET_NEW_SESSION)
def controller_deque_session():
    return svc.deque_session()


@app.on_event("startup")
async def startup_event():
    service_name = os.getenv("CONTAINER_NAME", "NO_NAME")
    service_port = int(os.getenv("MY_PORT", "8080"))

    register_service(service_name, service_port)


def register_service(service_name, port):
    c = consul.Consul(
        host=os.getenv("CONSUL_HOST", "consul"),
        port=int(os.getenv("CONSUL_PORT", "8500")),
    )
    service_id = f"{service_name}-{uuid.uuid4()}"
    address = os.environ.get('CONTAINER_NAME', 'NOT SET')

    c.agent.service.register(
        name=service_name,
        service_id=service_id,
        address=address,
        port=port,
        tags=["urlprefix-/" + service_name],
        check={
            "http": f"http://{address}:{port}/health",
            "interval": "3s",
            "DeregisterCriticalServiceAfter": "8s",
        },
    )
    print(f"Registered {service_name} with ID {service_id} and address {address}")


