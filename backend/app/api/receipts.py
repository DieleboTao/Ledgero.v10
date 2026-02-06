from fastapi import APIRouter, UploadFile, File, Depends
import os, shutil, uuid
from app.db import SessionLocal
from app.models import Receipt

router = APIRouter()
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "/app/uploads")

@router.post("/", status_code=201)
def upload_receipt(file: UploadFile = File(...), business_id: int = 1, db=Depends(SessionLocal)):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    ext = os.path.splitext(file.filename)[1]
    fname = f"{uuid.uuid4().hex}{ext}"
    path = os.path.join(UPLOAD_FOLDER, fname)
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    receipt = Receipt(business_id=business_id, filename=fname, content_type=file.content_type, uploaded_by=1)
    db.add(receipt)
    db.commit()
    db.refresh(receipt)
    return {"id": receipt.id, "filename": fname}
