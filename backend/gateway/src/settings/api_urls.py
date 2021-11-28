from dataclasses import dataclass


@dataclass(frozen=True)
class UserAPIUrls:
    base: str = "http://users:8001/users"
    register: str = f"{base}/register"
    login: str = f"{base}/login"
    all: str = f"{base}/"


@dataclass(frozen=True)
class TokenAPIUrls:
    base: str = "http://users:8001/token"
    verify: str = f"{base}/verify"


@dataclass(frozen=True)
class ProductAPIUrls:
    base: str = "http://products:8002/products"
    all: str = f"{base}/"


@dataclass(frozen=True)
class APIUrls:
    user: UserAPIUrls = UserAPIUrls()
    token: TokenAPIUrls = TokenAPIUrls()
    product: ProductAPIUrls = ProductAPIUrls()


api_urls = APIUrls()
