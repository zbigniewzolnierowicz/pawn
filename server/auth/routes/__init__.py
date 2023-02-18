from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server.auth import commands, schemas
from server.utils.db import get_db

router = APIRouter()


@router.post("/create")
async def create_user(
    user_to_create: schemas.CreateUser, db: Session = Depends(get_db),
) -> schemas.PublicUserData:
    return commands.create_user_command(db=db, user_data=user_to_create) 
