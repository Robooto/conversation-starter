from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import models, crud
from app.database import engine
from app.routes.v1 import api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Conversations")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    print('on starting up')
    crud.seed_db()
