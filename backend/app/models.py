from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from datetime import datetime
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False, unique=True)  # One wallet per user
    balance = Column(Float, default=0.0)
    payments = relationship("Payment", back_populates="wallet")

    def credit(self, amount):
            """ Add funds to the wallet """
            self.balance += amount

    def debit(self, amount):
        """ Deduct funds if sufficient balance is available """
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False


class Payment(Base):
    __tablename__ = "payments"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("wallets.user_id"), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="pending")  # pending, completed, failed
    timestamp = Column(DateTime, default=datetime.utcnow)

    wallet = relationship("Wallet", back_populates="payments")


class SyncLog(Base):
    __tablename__ = "sync_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    status = Column(String, nullable=False)  # success or failed
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)