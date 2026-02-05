from fastapi import FastAPI
from .database import engine, Base
from .routers import extraction

app = FastAPI(title="The Vibe Collective API")

# Include routers
app.include_router(extraction.router, prefix="/api", tags=["extraction"])

@app.get("/")
def read_root():
    return {"message": "Welcome to The Vibe Collective API"}
