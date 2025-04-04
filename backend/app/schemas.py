from pydantic import BaseModel

class WalletCreate(BaseModel):
    user_id: str
    balance: float = 0.0

class WalletResponse(WalletCreate):
    id: str
