from fastapi import FastAPI
import asyncio
import uvicorn
import os
from app.database import Base, engine
from app.routers.wallet_routes import router as wallet_router
from app.routers.payment_routes import router as payment_router
from app.routers.sync_routes import router as sync_router
from app.tasks.sync import check_network_and_sync


Base.metadata.create_all(bind=engine)  # Create tables on startup

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(check_network_and_sync())


app.include_router(wallet_router, prefix="/api")
app.include_router(payment_router, prefix="/api")
app.include_router(sync_router, prefix="/api")


