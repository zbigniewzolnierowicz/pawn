from pydantic import BaseModel


class PydanticBase(BaseModel):
    class Config:
        orm_mode = True
