from fastapi import FastAPI
from app.exceptions.global_exception_handler import register_global_exception_handlers
from app.routers.employee_router import router as employee_router
from app.database.database import Base, engine
from app.models.employee import Employee


app = FastAPI(
    title = "Employee AI Platform",
    description = "AI-powered Employee Management Platform",
    version = "1.0.0"
)
register_global_exception_handlers(app)
# Create the database tables
Base.metadata.create_all(bind=engine)


app.include_router(employee_router)

