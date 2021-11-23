from dataclasses import dataclass, field


@dataclass(frozen=True)
class UserAPIUrls:
    list: str = "users/"
    detail: str = "users/{user_id}"
    register: str = "users/register"


@dataclass(frozen=True)
class APIUrls:
    users: UserAPIUrls = UserAPIUrls()
