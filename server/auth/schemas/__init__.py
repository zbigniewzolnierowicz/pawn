from pydantic import EmailStr

from server.utils import PydanticBase


class UserBase(PydanticBase):
    email: EmailStr


class CreateUser(UserBase):
    password: str


class UserTokenRequest(UserBase):
    password: str


class PublicUserData(UserBase):
    pass
