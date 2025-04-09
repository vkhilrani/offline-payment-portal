# app/routers/sync_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Payment

router = APIRouter()


@router.post("/sync")
def sync_offline_transactions(db: Session = Depends(get_db)):
    pending_payments = db.query(Payment).filter(Payment.status == "pending").all()

    for payment in pending_payments:
        # For now we just mark them as completed
        payment.status = "completed"

    db.commit()
    return {"synced_count": len(pending_payments)}
