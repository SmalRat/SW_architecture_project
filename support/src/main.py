from fastapi import FastAPI

app = FastAPI(title="Support")


@app.get("/", tags=["main page"])
async def root():
    return "Support"
