from dataclasses import dataclass

from src.settings.hosts import ServiceSettings

service_settings = ServiceSettings()


@dataclass(frozen=True)
class UserAPIUrls:
    base: str = f"http://{service_settings.USERS_ADDRESS}/users"
    register: str = f"{base}/register"
    login: str = f"{base}/login"
    all: str = f"{base}/"
    me: str = f"{base}/me"


@dataclass(frozen=True)
class TokenAPIUrls:
    base: str = f"http://{service_settings.USERS_ADDRESS}/token"
    verify: str = f"{base}/verify"


@dataclass(frozen=True)
class ProductAPIUrls:
    base: str = f"http://{service_settings.PRODUCTS_ADDRESS}/products"
    all: str = f"{base}/"
    detail: str = f"{base}/{{}}"


@dataclass(frozen=True)
class APIUrls:
    user: UserAPIUrls = UserAPIUrls()
    token: TokenAPIUrls = TokenAPIUrls()
    product: ProductAPIUrls = ProductAPIUrls()


api_urls = APIUrls()
