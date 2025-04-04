# create_tables.py
from app.database import engine, Base
from app.models import Wallet  # Import all models here

Base.metadata.create_all(bind=engine)
