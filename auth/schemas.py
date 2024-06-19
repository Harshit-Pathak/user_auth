import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class UserCreateModel(BaseModel):
    name: str
    email: str
    password:str


class UserModel(BaseModel):
    uid: uuid.UUID
    name: str
    email: str


class UserLoginModel(BaseModel):
    email: str
    password: str