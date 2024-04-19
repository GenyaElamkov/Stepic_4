from enum import IntEnum, Enum


class HTTPTranslateRus(Enum):
    CONTINUE = "информация"
    OK = "успех"
    USE_PROXY = "перенаправление"
    NOT_FOUND = "ошибка клиента"
    BAD_GATEWAY = "ошибка сервера"


class HTTPStatusCodes(IntEnum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        translate = HTTPTranslateRus
        return translate[self.name].value


# INPUT DATA:

# TEST_1:
print(HTTPStatusCodes.OK.info())
print(HTTPStatusCodes.OK.code_class())

# TEST_2:
print(HTTPStatusCodes.CONTINUE.info())
print(HTTPStatusCodes.CONTINUE.code_class())

# TEST_3:
print(HTTPStatusCodes.USE_PROXY.info())
print(HTTPStatusCodes.USE_PROXY.code_class())

# TEST_4:
print(HTTPStatusCodes.NOT_FOUND.info())
print(HTTPStatusCodes.NOT_FOUND.code_class())

# TEST_5:
print(HTTPStatusCodes.BAD_GATEWAY.info())
print(HTTPStatusCodes.BAD_GATEWAY.code_class())

# TEST_6:
for instance in HTTPStatusCodes:
    print(f"{instance.name} -> {instance.value}")
