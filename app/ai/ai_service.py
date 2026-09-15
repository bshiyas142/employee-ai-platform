from app.ai.ai_client import AIClient
from app.exceptions.employee_exceptions import EmployeeNotFoundException
from app.models.employee import Employee
from app.repositories.employee_repository import EmployeeRepository
from app.ai.prompts.prompt_builder import PromptBuilder
from app.schemas.ai_schema import AIQuestionRequest
from app.schemas.employee_query import EmployeeQuery
class AIService:

    def __init__(self):
        self.ai_client = AIClient()
        self.employee_repository = EmployeeRepository()

    def summarize_employee(self, employee_id: str) -> str:
        employee = self.employee_repository.find_by_id(employee_id)
        if employee is None:
            raise  EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")

        prompt = PromptBuilder.employee_summary(employee)
    

        summary = self.ai_client.generate_response(prompt)
        return summary

    def understand_employee_query(self, question: AIQuestionRequest) -> EmployeeQuery:
        prompt = PromptBuilder.employee_query(question)
        structured_query = self.ai_client.generate_structured_response(prompt, EmployeeQuery)
        return structured_query