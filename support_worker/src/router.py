from fastapi import FastAPI
from support_worker.src.service import SupportWorkerService

SUPPORT_WORKER_SERVICE_GET_NEW_SESSION = "/deque_request"

app = FastAPI(title="Support")

svc = SupportWorkerService()

@app.get("/", tags=["support page"])
async def root():
    return "Support"


@app.get(SUPPORT_WORKER_SERVICE_GET_NEW_SESSION)
def controller_deque_session():
    return svc.deque_session()


