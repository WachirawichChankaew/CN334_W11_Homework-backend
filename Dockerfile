# ใช้ Python 3.10 เวอร์ชันเล็ก (slim) เพื่อให้โหลดไวและกินพื้นที่น้อย
FROM python:3.10-slim

# ตั้งค่า Directory เริ่มต้นใน Container
WORKDIR /app

# ก๊อปปี้ไฟล์ requirements.txt เข้าไปก่อนเพื่อติดตั้งไลบรารี
COPY requirements.txt .

# ติดตั้งไลบรารี
RUN pip install --no-cache-dir -r requirements.txt

# ก๊อปปี้ไฟล์โค้ดทั้งหมด (รวมถึง main.py) เข้าไปใน Container
COPY . .

# เปิด Port 8000 ให้ภายนอกเชื่อมต่อได้
EXPOSE 8000

# คำสั่งรัน FastAPI เมื่อ Container เริ่มทำงาน
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]