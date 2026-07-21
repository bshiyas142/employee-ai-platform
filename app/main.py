from fastapi import FastAPI
from app.routers.employee_router import router as employee_router
app = FastAPI(
    title = "Employee AI Platform",
    description = "AI-powered Employee Management Platform",
    version = "1.0.0"
)
app.include_router(employee_router)

