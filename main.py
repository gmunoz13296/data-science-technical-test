from fastapi import FastAPI
from routers import classifier

app = FastAPI(
    title="My Modern FastAPI Service",
    version="1.0.0",
    description="Welcome!",
)

app.include_router(classifier.router)

@app.get("/")
async def root():
    return {"message": "Welcome!"}
