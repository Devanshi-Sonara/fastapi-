from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from .routers import post, user, auth
from fastapi.middleware.cors import CORSMiddleware

# Initialize database models
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# General route
@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

# Optional startup/shutdown events
@app.on_event("startup")
async def startup_event():
    print("Application is starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Application is shutting down...")
