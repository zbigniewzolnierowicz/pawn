from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String

from ...db import Base


class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    password_hash = Column(String)
    is_active = Column(Boolean, default=True)
    is_registration_confirmed = Column(Boolean, default=False)

class CreateUser(BaseModel):
    email: str
    password: str

class UserTokenRequest(BaseModel):
    email: str
    password: str
