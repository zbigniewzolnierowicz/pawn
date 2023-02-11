from fastapi import APIRouter, Depends, HTTPException
from http_constants.status import HttpStatus
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.auth import models, schemas
from server.db import get_db

router = APIRouter()


@router.post("/create")
async def create_user(
    user_to_create: schemas.CreateUser, db: Session = Depends(get_db),
) -> schemas.PublicUserData:
    db_user = models.UserModel(
        email=user_to_create.email,
        password_hash=user_to_create.password + "fakehash",
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError as ex:
        db.rollback()
        raise HTTPException(status_code=HttpStatus.FORBIDDEN, detail="User already exists.") from ex
    except Exception as ex:
        raise HTTPException(
            status_code=HttpStatus.INTERNAL_SERVER_ERROR, detail="There was an internal database error.",
        ) from ex
    else:
        public_user = schemas.PublicUserData(**db_user.__dict__)
        return public_user
