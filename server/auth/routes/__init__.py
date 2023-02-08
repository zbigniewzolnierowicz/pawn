from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_user(email: str):
    return
