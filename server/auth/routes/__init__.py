from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from server.auth import schemas, models
from server.db import get_db

router = APIRouter()


@router.post("/create")
async def create_user(
    user_to_create: schemas.CreateUser, db: Session = Depends(get_db)
) -> schemas.PublicUserData:
    db_user = models.UserModel(
        email=user_to_create.email, password_hash=user_to_create.password + "fakehash"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    public_user = schemas.PublicUserData(**db_user.__dict__)
    return public_user
