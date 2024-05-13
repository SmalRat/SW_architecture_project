import support.src.models
import support.src.service
import support.src.utils
from support.src.router import support
from fastapi import FastAPI


app = FastAPI(title="Support")

app.include_router(support, tags=["support"])


@app.get("/", tags=["main page"])
async def root():
    return "Test"
