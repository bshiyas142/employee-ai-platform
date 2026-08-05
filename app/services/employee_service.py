

from app.exceptions.employee_exceptions import EmployeeNotFoundException
from app.models.employee import Employee

from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee_schema import EmployeeCreateRequest, EmployeeUpdateRequest, EmploymentStatus, EmployeeResponse


class EmployeeService:
    def __init__(self):
        self.employee_repository = EmployeeRepository()

    def create_employee(self, employee_request: EmployeeCreateRequest):
        employee = Employee(
            employee_id=self.get_last_employee_id(),
            first_name=employee_request.first_name,
            last_name=employee_request.last_name,
            email=employee_request.email,
            phone_number=employee_request.phone_number,
            date_Of_joining=employee_request.date_Of_joining,
            department_id=employee_request.department_id,
            manager_id=employee_request.manager_id,
            hr_id=employee_request.hr_id,
            role=employee_request.role,
            designation=employee_request.designation,
            employment_status=EmploymentStatus.ACTIVE
        )
        self.employee_repository.save(employee)
        return self._to_response(employee)

    def _to_response(self, employee: Employee) -> EmployeeResponse:
        return EmployeeResponse(
            employee_id=employee.employee_id,
            first_name=employee.first_name,
            last_name=employee.last_name,
            email=employee.email,
            phone_number=employee.phone_number,
            date_Of_joining=employee.date_Of_joining,
            department_id=employee.department_id,
            manager_id=employee.manager_id,
            hr_id=employee.hr_id,
            role=employee.role,
            designation=employee.designation,
            employment_status=employee.employment_status
        )
    

    def get_employee(self, employee_id: str) -> EmployeeResponse:
        employee = self.employee_repository.find_by_id(employee_id)
        if employee is None:
            raise EmployeeNotFoundException(employee_id)
        return self._to_response(employee)

    def get_all_employees(self) -> list[EmployeeResponse]:
        employees = self.employee_repository.find_all()
        return [
            self._to_response(employee)
            for employee in employees
         ]

    def update_employee(self, employee_id: str, employee_request: EmployeeUpdateRequest) -> EmployeeResponse:
        employee = self.employee_repository.find_by_id(employee_id)
        if employee is None:
            raise ValueError(f"Employee with ID {employee_id} not found")

        update_data = employee_request.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(employee, field, value)

        self.employee_repository.update(employee)
        return self._to_response(employee)

    def delete_employee(self, employee_id: str):
        employee = self.employee_repository.find_by_id(employee_id)
        if employee is None:
            raise EmployeeNotFoundException(employee_id)
        employee.employment_status = EmploymentStatus.TERMINATED
        self.employee_repository.update(employee)

    def get_last_employee_id(self) -> str:
        last_employee_id = self.employee_repository.get_last_employee_id()
        if last_employee_id is None:
            return "EMP000001"
        number = int(last_employee_id.replace("EMP", ""))
        number += 1
        return f"EMP{number:06d}"