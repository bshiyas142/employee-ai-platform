
from app.models.employee import Employee
from app.storage.memory_store import employees


class EmployeeRepository:

    def save(self, employee: Employee):
        employees[employee.employee_id] = employee

    def find_all(self):
        return list(employees.values())

    def find_by_id(self, employee_id: str):
        return employees.get(employee_id)