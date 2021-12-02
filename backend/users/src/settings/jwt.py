from pydantic import BaseSettings


class AuthJWTSettings(BaseSettings):
    authjwt_secret_key: str
    authjwt_access_token_expires: int = 24 * 3600
