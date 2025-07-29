from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database import engine, Base
from .models import module as models
from .routes import module

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup code here
    Base.metadata.create_all(bind=engine)
    yield
    # shutdown code here

app = FastAPI(title="modulr", lifespan=lifespan)

app.include_router(module.router)
