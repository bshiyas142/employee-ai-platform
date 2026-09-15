from fastapi import APIRouter
from app.ai.ai_client import AIClient
from app.ai.ai_service import AIService
from app.schemas.ai_schema import AIQuestionRequest

router = APIRouter(prefix="/ai", tags=["AI"])

client = AIClient()
ai_service = AIService()

@router.get("/test")
def test_ai():
    return {
        "response": client.generate_response("Reply with exactly one sentence saying Hello from the Employee AI Platform.")
    }

@router.get("/summarize/{employee_id}")
def summarize_employee(employee_id: str):
    return {
        "summary": ai_service.summarize_employee(employee_id)
    }


@router.post("/query")
def understand_employee_query(question: AIQuestionRequest):
    return ai_service.understand_employee_query(question)
