from fastapi import APIRouter

from app.schemas.employee_schema import EmployeeCreateRequest, EmployeeResponse
from app.services.employee_service import EmployeeService

router = APIRouter(prefix="/employees", tags=["Employees"])

employee_service = EmployeeService()

@router.post("", response_model=EmployeeResponse)
def create_employee(employee_request: EmployeeCreateRequest):
    return employee_service.create_employee(employee_request)


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: str):
    return employee_service.get_employee(employee_id)

@router.get("", response_model=list[EmployeeResponse])
def get_all_employees():
    return employee_service.get_all_employees()