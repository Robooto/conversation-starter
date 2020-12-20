from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import models, crud
from app.database import engine
from app.routes.v1 import api_router as v1_api_router
from app.routes.v2 import api_router as v2_api_router

models.Base.metadata.create_all(bind=engine)

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
app.include_router(v1_api_router, prefix="/api/v1")
app.include_router(v2_api_router, prefix="/api/v2")


@app.on_event("startup")
async def startup_event():
    print('on starting up')
    crud.seed_db()
