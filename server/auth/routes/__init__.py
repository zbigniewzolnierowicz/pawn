from fastapi import APIRouter, Depends, Request

router = APIRouter()

@router.post("/create")
async def create_user():
    return
