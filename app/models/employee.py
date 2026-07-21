import datetime
from typing import Optional

from pydantic import BaseModel


from app.schemas.employee_schema import Designation, EmploymentStatus, Role

class Employee(BaseModel):
    employee_id: str
    first_name: str
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    date_Of_joining: datetime.date
    department_id: str
    manager_id: Optional[str] = None
    hr_id: Optional[str] = None
    role: Role
    designation: Designation
    employment_status: EmploymentStatus