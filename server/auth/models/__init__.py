from sqlalchemy import Boolean, Column, Integer, String

from server.db import Base


class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, unique=True)
    password_hash = Column(String)
    is_active = Column(Boolean, default=True)
    is_registration_confirmed = Column(Boolean, default=False)
