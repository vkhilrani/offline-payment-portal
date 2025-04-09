from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Payment, Wallet
from app.schemas import PaymentCreate, PaymentResponse

router = APIRouter()


@router.post("/payments/", response_model=PaymentResponse)
def create_payment(payment_data: PaymentCreate, db: Session = Depends(get_db)):
    wallet = db.query(Wallet).filter(Wallet.user_id == payment_data.user_id).first()
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    if wallet.balance < payment_data.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    new_payment = Payment(user_id=payment_data.user_id,
                          amount=payment_data.amount, status="pending")
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return new_payment
