class Account:
    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self._password = password

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, login: str) -> AttributeError:
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self) -> str:
        pas = hash_function(self._password)
        return pas

    @password.setter
    def password(self, password) -> None:
        self._password = password

def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10**9


account = Account('timyr-guev', 'lovebeegeek')
try:
    account.login = 'timyrik30'
except AttributeError as e:
    print(e)