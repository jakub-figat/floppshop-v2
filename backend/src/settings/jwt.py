from pydantic import BaseSettings


class AuthJWTConfig(BaseSettings):
    authjwt_secret_key: str
