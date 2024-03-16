from datetime import datetime
from typing import NamedTuple


class User(NamedTuple):
    username: str
    bithday: datetime


def get_name(user: User) -> User:
    return User(username='Genya', bithday=datetime(1984,12,23))


user = User

print(get_name(user))
