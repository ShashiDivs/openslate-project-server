from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import users, projects
import os

app = FastAPI(
    title="OpenSlate AI Engineering API",
    description = "Backend API for OpenSlate AI Engineering Project",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(users.router)
app.include_router(projects.router)


@app.get("/")
async def root():
    return {"message":"Openslate AI Engineering app is running!"}

@app.get("/health")
async def health_check():
    return {
        "status":"healthy",
        "version":"1.0.1"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=8000, reload=True)