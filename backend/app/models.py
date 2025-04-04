from sqlalchemy import Column, String, Float
from .database import Base
import uuid

class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False, unique=True)  # One wallet per user
    balance = Column(Float, default=0.0)
    
    def credit(self, amount):
            """ Add funds to the wallet """
            self.balance += amount

    
    def debit(self, amount):
        """ Deduct funds if sufficient balance is available """
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

   
