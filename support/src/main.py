from support.src.router import support
from fastapi import FastAPI
import consul
import os
import uuid
import socket
import logging

app = FastAPI(title="Support")

app.include_router(support, tags=["support"])


@app.get("/", tags=["main page"])
async def root():
    return "Main page of the support service"


@app.on_event("startup")
async def startup_event():
    c = consul.Consul(
        host=os.getenv("CONSUL_HOST", "consul"),
        port=int(os.getenv("CONSUL_PORT", "8500")),
    )

    service_name = "support"
    service_port = int(os.getenv("SUPPORT_SERVICE_INTERNAL_PORT", "80"))
    service_id = f"{service_name}-{socket.gethostname()}"

    c.agent.service.register(
        name=service_name,
        service_id=service_id,
        address=socket.gethostname(),
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
