from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database import engine, Base
from .models import module as model_module
from .routes import module as module_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup code here
    Base.metadata.create_all(bind=engine)
    yield
    # shutdown code here

app = FastAPI(title="modulr", lifespan=lifespan)

app.include_router(module_routes.router)
