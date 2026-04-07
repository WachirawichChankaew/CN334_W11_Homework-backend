from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
# ดึง router มาจาก app/crud.py
from app.crud import router as ropa_router 

# สร้างตารางในฐานข้อมูล (ถ้ายังไม่มี)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ROPA Management API")

# ตั้งค่า CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# นำเข้า Router ของ ROPA เข้ามาในแอป
app.include_router(ropa_router)