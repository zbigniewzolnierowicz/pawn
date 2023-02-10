from server.utils import PydanticBase


class UserBase(PydanticBase):
    email: str


class CreateUser(UserBase):
    password: str


class UserTokenRequest(UserBase):
    email: str
    password: str


class PublicUserData(UserBase):
    pass
