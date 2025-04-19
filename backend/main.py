from fastapi import FastAPI
from backend.auth import router as auth_router
from backend.gmail import router as gmail_router
from backend.aggregate import router as report_router



app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(gmail_router, prefix="/mail")
app.include_router(report_router, prefix="/report")
