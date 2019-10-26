from fastapi import FastAPI

from app.routes.api import api_router

app = FastAPI(title="Conversations")
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def home():
    return {"Hello": "World"}
