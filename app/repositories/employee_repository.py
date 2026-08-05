
from app.models.employee import Employee

from app.database.database import SessionLocal
from app.schemas.employee_schema import EmploymentStatus

class EmployeeRepository:

    def __init__(self):
        self.db = SessionLocal()
    def save(self, employee: Employee):
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)

    def find_all(self):
        return (self.db.query(Employee)
                .filter(Employee.employment_status != EmploymentStatus.TERMINATED).all())

    def find_by_id(self, employee_id: str):
        return self.db.query(Employee).filter(Employee.employee_id == employee_id).first()
    

    def update(self, employee: Employee):
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def get_last_employee_id(self):
        last_employee = self.db.query(Employee).order_by(Employee.employee_id.desc()).first()
        return last_employee.employee_id if last_employee else None