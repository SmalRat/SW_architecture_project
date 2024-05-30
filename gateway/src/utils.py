from fastapi import FastAPI, HTTPException
import consul
import random
import os
import logging

def get_service_url(service_name: str) -> str:
    c = consul.Consul(
        host=os.getenv("CONSUL_HOST", "consul"),
        port=int(os.getenv("CONSUL_PORT", "8500")),
    )
    index, services = c.health.service(service_name, passing=True)
    # print(services)
    if not services:
        raise HTTPException(status_code=404, detail=f"Service {service_name} not found")

    services = [
        service
        for service in services
        if service["Checks"][0]["Status"] == "passing"
    ]
    service_urls = [
        f"http://{service['Service']['Address']}:{service['Service']['Port']}"
        for service in services
    ]
    logging.info(f"{service_name} services: {service_urls}")
    random_service = random.choice(service_urls)

    return random_service