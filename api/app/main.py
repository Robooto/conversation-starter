from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes.api import api_router

app = FastAPI(title="Conversations")
origins = [
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api/v1")
