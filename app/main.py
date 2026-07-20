from fastapi import FastAPI

app = FastAPI(
    title = "Employee AI Platform",
    description = "AI-powered Employee Management Platform",
    version = "1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to the Employee AI Platform!"}

@app.get("/health")
def health_check():
    return {"status": "UP"}
