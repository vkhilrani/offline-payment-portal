from fastapi import FastAPI
from app.database import Base, engine
from app.routers.wallet_routes import router as wallet_router

Base.metadata.create_all(bind=engine)  # Create tables on startup

app = FastAPI()

app.include_router(wallet_router, prefix="/api")
