from fastapi import APIRouter

router = APIRouter()

@router.post("/create")
async def create_user():
    return
