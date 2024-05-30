from fastapi import FastAPI
from worker.src.service import SupportWorkerService
import consul
import os
import logging
import socket

SUPPORT_WORKER_SERVICE_GET_NEW_SESSION = "/deque_request"

app = FastAPI(title="Support worker")

svc = SupportWorkerService()

@app.get("", tags=["support worker page"])
async def root():
    return "Support"



@app.get(SUPPORT_WORKER_SERVICE_GET_NEW_SESSION)
def controller_deque_session():
    print("*"*100)
    return svc.deque_session()

@app.on_event("startup")
async def startup_event():
    c = consul.Consul(
        host=os.getenv("CONSUL_HOST", "consul"),
        port=int(os.getenv("CONSUL_PORT", "8500")),
    )

    service_name = "worker"
    service_port = int(os.getenv("WORKER_SERVICE_INTERNAL_PORT", "80"))
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

@app.get("/health")
def health_check():
    return {"status": "healthy"}


