from pydantic import BaseModel
from datetime import datetime


class WalletCreate(BaseModel):
    user_id: str
    balance: float = 0.0


class WalletResponse(WalletCreate):
    id: str


class PaymentCreate(BaseModel):
    user_id: str
    amount: float


class PaymentResponse(PaymentCreate):
    id: str
    status: str
    timestamp: datetime

