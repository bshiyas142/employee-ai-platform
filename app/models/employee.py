import datetime
from typing import Optional
from sqlalchemy import Column, String, Date, Enum
from app.database.database import Base


from app.schemas.employee_schema import Designation, EmploymentStatus, Role

class Employee(Base):
    __tablename__ = "employees"

    employee_id  =  Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    date_Of_joining = Column(Date, nullable=False)
    department_id = Column(String, nullable=False)
    manager_id = Column(String, nullable=True)
    hr_id = Column(String, nullable=True)
    role = Column(Enum(Role), nullable=False)
    designation = Column(Enum(Designation), nullable=False)
    employment_status = Column(Enum(EmploymentStatus), nullable=False)