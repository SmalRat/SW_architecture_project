from fastapi import FastAPI, HTTPException
import logging
from gateway.src.routers.app import app_admin, app_user
from gateway.src.routers.support import support
from gateway.src.routers.worker import worker
from gateway.src.routers.booking import booking

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

gateway_router = FastAPI()

gateway_router.include_router(app_admin, tags=["app"])
gateway_router.include_router(app_user, tags=["app"])
gateway_router.include_router(support, tags=["support"])
gateway_router.include_router(worker, tags=["worker"])
gateway_router.include_router(booking, tags=["booking"])
