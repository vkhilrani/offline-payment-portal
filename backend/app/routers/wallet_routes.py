from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Wallet
from app.schemas import WalletCreate, WalletResponse

router = APIRouter()

@router.post("/wallets/", response_model=WalletResponse)
def create_wallet(wallet_data: WalletCreate, db: Session = Depends(get_db)):
    existing_wallet = db.query(Wallet).filter(Wallet.user_id == wallet_data.user_id).first()
    if existing_wallet:
        raise HTTPException(status_code=400, detail="Wallet already exists")

    new_wallet = Wallet(user_id=wallet_data.user_id, balance=wallet_data.balance)
    db.add(new_wallet)
    db.commit()
    db.refresh(new_wallet)
    return new_wallet

@router.get("/wallets/{user_id}", response_model=WalletResponse)
def get_wallet(user_id: str, db: Session = Depends(get_db)):
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return wallet

@router.put("/wallets/{user_id}/credit")
def credit_wallet(user_id: str, amount: float, db: Session = Depends(get_db)):
    """ Add funds to a user's wallet """
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    
    wallet.credit(amount)
    db.commit()
    return {"message": "Wallet credited", "new_balance": wallet.balance}

@router.put("/wallets/{user_id}/debit")
def debit_wallet(user_id: str, amount: float, db: Session = Depends(get_db)):
    """ Deduct funds from a user's wallet if sufficient balance """
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    
    if wallet.debit(amount):
        db.commit()
        return {"message": "Wallet debited", "new_balance": wallet.balance}
    else:
        raise HTTPException(status_code=400, detail="Insufficient balance")