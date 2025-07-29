from fastapi import FastAPI
from app.routes import module

app = FastAPI(title="modulr")

app.include_router(module.router)
