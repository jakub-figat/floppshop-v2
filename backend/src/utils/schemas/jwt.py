from pydantic import BaseModel


class AccessTokenOutputSchema(BaseModel):
    access: str
