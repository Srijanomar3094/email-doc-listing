from fastapi import APIRouter, HTTPException
from passlib.hash import bcrypt
from pymongo import MongoClient
from backend.models import User
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["emailApp"]
users = db["users"]

@router.post("/register")
def register(user: User):
    if users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    hashed_pw = bcrypt.hash(user.password)
    users.insert_one({"email": user.email, "password": hashed_pw})
    return {"message": "User created"}

@router.post("/login")
def login(user: User):
    record = users.find_one({"email": user.email})
    if not record or not bcrypt.verify(user.password, record["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}
