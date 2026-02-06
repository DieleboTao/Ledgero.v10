from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.db import SessionLocal
from app.models import Transaction

router = APIRouter()

class TransactionIn(BaseModel):
    business_id: int
    amount: float
    type: str
    category: str = None
    description: str = None

@router.post("/")
def create_tx(tx: TransactionIn, db=Depends(SessionLocal)):
    t = Transaction(**tx.dict())
    db.add(t)
    db.commit()
    db.refresh(t)
    return {"id": t.id, "business_id": t.business_id, "amount": float(t.amount), "type": t.type, "category": t.category, "description": t.description}

@router.get("/")
def list_transactions(business_id: int = 1, db=Depends(SessionLocal)):
    txs = db.query(Transaction).filter_by(business_id=business_id).all()
    return [{"id": t.id, "amount": float(t.amount), "type": t.type, "category": t.category, "description": t.description, "date": t.date.isoformat()} for t in txs]
