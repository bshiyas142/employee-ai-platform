class EmployeeNotFoundException(Exception):
   def __init__(self, employee_id: str):
     super().__init__(f"Employee with ID {employee_id} not found.")