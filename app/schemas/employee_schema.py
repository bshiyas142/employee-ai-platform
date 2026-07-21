from enum import Enum

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date


class Role(str, Enum):
    EMPLOYEE = "EMPLOYEE"
    MANAGER = "MANAGER"
    HR = "HR"
    EXECUTIVE = "EXECUTIVE"

class Designation(str, Enum):
    SOFTWARE_ENGINEER = "Software Engineer"
    SENIOR_SOFTWARE_ENGINEER = "Senior Engineer"
    TECHNICAL_LEAD = "Technical Lead"
    ARCHITECT = "Architect"
    ENGINEERING_MANAGER = "Engineering Manager"
    HR_EXECUTIVE = "HR Executive"
    CEO = "CEO"


class EmploymentStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ON_LEAVE = "ON_LEAVE"
    TERMINATED = "TERMINATED"
    RESIGNED = "RESIGNED"

class EmployeeCreateRequest(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=50, description="First name of the employee")
    last_name: Optional[str] = Field(None, max_length=50, description="Last name of the employee")
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    date_Of_joining: date
    department_id: str
    manager_id: Optional[str] = None
    hr_id: Optional[str] = None
    role: Role
    designation: Designation
    employment_status: EmploymentStatus


class EmployeeResponse(BaseModel):
    employee_id: str
    first_name: str
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    date_Of_joining: date
    department_id: str
    manager_id: Optional[str] = None
    hr_id: Optional[str] = None
    role: Role
    designation: Designation
    employment_status: EmploymentStatus

