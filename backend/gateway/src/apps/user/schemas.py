import datetime as dt
from uuid import UUID

from humps import camelize
from pydantic import BaseModel, Field


class UserBaseSchema(BaseModel):
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    username: str = Field(..., max_length=30)
    email: str
    date_of_birth: dt.date

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class UserLoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class UserRegisterSchema(UserBaseSchema):
    password: str = Field(..., min_length=8, max_length=32)
    password_2: str = Field(..., min_length=8, max_length=32)


class UserUpdateSchema(BaseModel):
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    username: str = Field(..., max_length=30)
    email: str
    date_of_birth: dt.date

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class UserOutputSchema(UserBaseSchema):
    id: UUID
    is_active: bool


class AccessTokenOutputSchema(BaseModel):
    access: str

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True
