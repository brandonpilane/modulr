from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Modulr backend is running!"}
