from fastapi import APIRouter, Response
import csv
from io import StringIO
from app.db import SessionLocal
from app.models import Transaction

router = APIRouter()

@router.get("/pnl")
def pnl_csv(business_id: int = 1):
    db = SessionLocal()
    txs = db.query(Transaction).filter_by(business_id=business_id).all()
    income = sum([float(t.amount) for t in txs if t.type == "income"])
    expenses = sum([float(t.amount) for t in txs if t.type == "expense"])
    net = income - expenses

    buf = StringIO()
    writer = csv.writer(buf)
    writer.writerow(["Ledgero Profit & Loss"])
    writer.writerow(["Income", income])
    writer.writerow(["Expenses", expenses])
    writer.writerow(["Net", net])
    return Response(content=buf.getvalue(), media_type="text/csv")
