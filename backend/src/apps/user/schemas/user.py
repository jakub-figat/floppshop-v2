import datetime as dt
from typing import Any
from uuid import UUID

from dateutil.relativedelta import relativedelta
from pydantic import BaseModel, Field, validate_email, validator


class UserBaseSchema(BaseModel):
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    username: str = Field(..., max_length=30)
    email: str
    date_of_birth: dt.date


class UserLoginInputSchema(BaseModel):
    email: str
    password: str


class UserRegisterInputSchema(UserBaseSchema):
    password: str = Field(..., min_length=8, max_length=32)
    password_2: str = Field(..., min_length=8, max_length=32)

    class Config:
        orm_mode = True

    @validator("password_2")
    def validate_passwords(cls, password_2: str, values: dict[str, Any]) -> str:
        if password_2 != values["password"]:
            raise ValueError("Second password differs from first one.")

        return password_2

    @validator("date_of_birth")
    def validate_date_of_birth(cls, date_of_birth: dt.date) -> dt.date:
        if date_of_birth >= dt.date.today():
            raise ValueError("Date of birth must be in the past.")

        return date_of_birth

    @validator("email")
    def validate_email(cls, email: str) -> str:
        validate_email(email)
        return email


class UserInputSchema(UserBaseSchema):
    pass


class UserOutputSchema(UserBaseSchema):
    id: UUID
    is_active: bool = True

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "e2ceeb4b-b602-48f3-aa61-d763237075a2",
                "first_name": "Małpian",
                "last_name": "Kowalsky",
                "username": "malpiankowalsky",
                "email": "malpiankowalsky@op.pl",
                "date_of_brith": "2020-01-01",
                "is_active": True,
            }
        }

    @property
    def age(self):
        return relativedelta(dt.date.today(), self.date_of_birth).years
