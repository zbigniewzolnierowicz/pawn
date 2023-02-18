from typing import Self, TypedDict

from fastapi import HTTPException, Request
from http_constants.status import HttpStatus
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from server.auth import models, schemas
from server.main import app


class UserCreationParams(TypedDict):
    db: Session
    user_data: schemas.CreateUser

class UserAlreadyExistsError(Exception):
    def __init__(self: Self, user: schemas.CreateUser) -> None:
        self.base_user = user

@app.exception_handler(UserAlreadyExistsError)
async def unicorn_exception_handler(request: Request, exc: UserAlreadyExistsError) -> JSONResponse:
    return JSONResponse(
        status_code=HttpStatus.CONFLICT,
        content={ "message": f"User with the following email already exists: {exc.base_user.email}"},
    )
    
def create_user_command(db: Session, user_data: schemas.CreateUser) -> schemas.PublicUserData:
    try:
        db_user = models.UserModel(
            email=user_data.email,
            password_hash=user_data.password + "fakehash",
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError as ex:
        db.rollback()
        raise UserAlreadyExistsError(user=user_data) from ex
    except Exception as ex:
        db.rollback()
        raise HTTPException(
            status_code=HttpStatus.INTERNAL_SERVER_ERROR, detail="There was an internal database error.",
        ) from ex
    else:
        public_user = schemas.PublicUserData(**db_user.__dict__)
        return public_user

def update_user(db: Session, user: models.UserModel, user_update: schemas.PublicUserData) -> schemas.PublicUserData:
    return schemas.PublicUserData(**user.__dict__)
