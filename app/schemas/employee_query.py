from datetime import date
from enum import Enum
from pydantic import BaseModel

class QueryOperation(str, Enum):
    LIST = "LIST",
    GET = "GET",
    COUNT = "COUNT"


class EmployeeQuery(BaseModel):
    operation: QueryOperation
    employee_id: str |None = None
    department_id: str |None = None
    designation: str |None = None
    employment_status: str |None = None
    joined_after: date |None = None
    joined_before: date |None = None