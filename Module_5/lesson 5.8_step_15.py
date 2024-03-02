class ProtectedObject:
    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __getattribute__(self, __name: str):
        __class__.error_attribute(__name)
        return object.__getattribute__(self, __name)

    def __setattr__(self, __name: str, __value) -> None:
        __class__.error_attribute(__name)
        return object.__setattr__(self, __name, __value)

    def __delattr__(self, __name: str) -> None:
        __class__.error_attribute(__name)
        object.__delattr__(self, __name)

    @classmethod
    def error_attribute(cls, __name):
        if __name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")


# INPUT DATA:

# TEST_1:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)

# TEST_2:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

try:
    user._password = "qwerty12345"
except AttributeError as e:
    print(e)

# TEST_3:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

try:
    del user._password
except AttributeError as e:
    print(e)

# TEST_4:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

del user.login
print("Успешное удаление атрибута")

# TEST_5:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")
print(object.__getattribute__(user, "login"))
print(object.__getattribute__(user, "_password"))

# TEST_6:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

try:
    user.__dict__["attr"] = 1
except AttributeError as e:
    print(e)

# TEST_7:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

try:
    print(user.__dict__)
except AttributeError as e:
    print(e)

# TEST_8:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

try:
    del user.__dict__["_password"]
except AttributeError as e:
    print(e)

# TEST_9:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

del user.login

try:
    print(user.login)
except AttributeError:
    print("Атрибут отсутствует")

# TEST_10:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

user.login = "Kamiya"
print(user.login)

user.nickname = "PG"
print(user.nickname)

# TEST_11:
user = ProtectedObject(login="PG_kamiya", _password="alreadybanned")

try:
    print(user._secret)
except AttributeError as e:
    print(e)

try:
    user._secret = "PG"
except AttributeError as e:
    print(e)

try:
    del user._secret
except Exception as e:
    print(e)
