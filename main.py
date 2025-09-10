from fastapi import FastAPI
from routers import classifier

app = FastAPI(
    title="My Modern FastAPI Service",
    version="1.0.0",
    description="A simple example of a modern FastAPI web API 🚀",
)

# Register routers
app.include_router(classifier.router)

@app.get("/")
async def root():
    return {"message": "Welcome to My Modern FastAPI Service 🚀"}
