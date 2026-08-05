from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions.employee_exceptions import EmployeeNotFoundException

def register_global_exception_handlers(app: FastAPI):
    @app.exception_handler(EmployeeNotFoundException)
    async def employee_not_found_exception_handler(request: Request, exc: EmployeeNotFoundException):
        return JSONResponse(
            status_code=404,
            content={"message": str(exc)},
        )