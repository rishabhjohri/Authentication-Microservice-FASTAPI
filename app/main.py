from fastapi import FastAPI
from app.routes import auth

app = FastAPI(title="Authentication Microservice")

app.include_router(auth.router, prefix="/api/auth")

@app.get("/")
async def root():
    return {"message": "Authentication Service is Running"}
