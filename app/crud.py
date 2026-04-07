from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import models
from app import schemas

# สร้าง Router (กำหนด prefix เป็น /ropa แค่ที่เดียว)
router = APIRouter(
    prefix="/ropa",
    tags=["ROPA"]
)

# ==========================================
# 1. Create (สร้างข้อมูลใหม่)
# สังเกตว่าใช้ "" ไม่มี / เพื่อรองรับ POST http://127.0.0.1:8000/ropa
# ==========================================
@router.post("", response_model=schemas.RopaResponse)
def create_ropa(ropa: schemas.RopaSchema, db: Session = Depends(get_db)):
    db_ropa = models.RopaRecord(**ropa.model_dump())
    db.add(db_ropa)
    db.commit()
    db.refresh(db_ropa)
    return db_ropa

# ==========================================
# 2. Read All (ดึงข้อมูลทั้งหมดแสดงในตาราง)
# ใช้ "" ไม่มี / เพื่อรองรับ GET http://127.0.0.1:8000/ropa
# ==========================================
@router.get("", response_model=List[schemas.RopaResponse])
def get_all_ropas(db: Session = Depends(get_db)):
    return db.query(models.RopaRecord).all()

# ==========================================
# 3. Read One (ดึงข้อมูล 1 แถวเพื่อไปโชว์หน้า Edit)
# อันนี้ต้องมี / เพราะต้องรับ ID เช่น GET http://127.0.0.1:8000/ropa/1
# ==========================================
@router.get("/{ropa_id}", response_model=schemas.RopaResponse)
def get_ropa(ropa_id: int, db: Session = Depends(get_db)):
    db_ropa = db.query(models.RopaRecord).filter(models.RopaRecord.id == ropa_id).first()
    if db_ropa is None:
        raise HTTPException(status_code=404, detail="ROPA record not found")
    return db_ropa

# ==========================================
# 4. Update (แก้ไขข้อมูล)
# PUT http://127.0.0.1:8000/ropa/1
# ==========================================
@router.put("/{ropa_id}", response_model=schemas.RopaResponse)
def update_ropa(ropa_id: int, ropa: schemas.RopaSchema, db: Session = Depends(get_db)):
    db_ropa = db.query(models.RopaRecord).filter(models.RopaRecord.id == ropa_id).first()
    if db_ropa is None:
        raise HTTPException(status_code=404, detail="ROPA record not found")
    
    update_data = ropa.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_ropa, key, value)
        
    db.commit()
    db.refresh(db_ropa)
    return db_ropa

# ==========================================
# 5. Delete (ลบข้อมูล)
# DELETE http://127.0.0.1:8000/ropa/1
# ==========================================
@router.delete("/{ropa_id}")
def delete_ropa(ropa_id: int, db: Session = Depends(get_db)):
    db_ropa = db.query(models.RopaRecord).filter(models.RopaRecord.id == ropa_id).first()
    if db_ropa is None:
        raise HTTPException(status_code=404, detail="ROPA record not found")
    
    db.delete(db_ropa)
    db.commit()
    return {"message": "Deleted successfully"}