from fastapi import FastAPI
from app.routes import modules

app = FastAPI(title="modulr")

app.include_router(modules.router)
