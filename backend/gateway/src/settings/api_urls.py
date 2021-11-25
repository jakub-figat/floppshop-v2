from dataclasses import dataclass


@dataclass(frozen=True)
class UserAPIUrls:
    base: str = "http://users:8001/users"
    register: str = f"{base}/register"
    login: str = f"{base}/login"
    all: str = f"{base}/"


@dataclass(frozen=True)
class APIUrls:
    user: UserAPIUrls = UserAPIUrls()


api_urls = APIUrls()
