from fastapi import FastAPI

app = FastAPI(
    title="IntelliWealth API",
    description="AI-Powered Personal Finance Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to IntelliWealth 🚀"
    }