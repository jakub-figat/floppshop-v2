from pydantic import BaseSettings


class AuthJWTSettings(BaseSettings):
    authjwt_secret_key: str
