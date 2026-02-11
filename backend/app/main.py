from fastapi import FastAPI
from app.db import engine
from app.models import Base

from app.api import transactions, receipts, reports
 
app = FastAPI(title="Ledgero API")
Base.metadata.create_all(bind=engine)

app.include_router(transactions.router, prefix="/api/transactions", tags=["transactions"])
app.include_router(receipts.router, prefix="/api/receipts", tags=["receipts"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])

@app.get("/")
def root():
    return {"status": "Ledgero API is running"}
