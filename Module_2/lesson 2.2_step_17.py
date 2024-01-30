"""
Функция pluck()
Реализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:

data — словарь произвольной вложенности
path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно
Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность ключей, например, key1.key2, то возвращаемым значением функции должно быть значение по ключу key2 из словаря data[key1]. Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет, функция должна вернуть значение default.

https://stepik.org/lesson/794484/step/17?unit=797232
"""


def pluck(data: dict, path: str, default="None"):
    if path in data:
        return data[path]

    path = path.split(".")
    for _ in data:
        try:
            if isinstance(data[path[0]], dict):
                data = data[path[0]]
                del path[0]
                return pluck(data, ".".join(path), default)
        except KeyError:
            return default


if __name__ == "__main__":
    d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
    print(pluck(d, "x"))

    d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
    print(pluck(d, "a.b"))

    d = {"a": {"b": {"c": {"d": {"e": 4}}}}}
    print(pluck(d, "a.b.c"))

    d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
    print(pluck(d, "c.d"))

    d = {"a": {"b": 5, "z": 20}, "c": {"d": 3}, "x": 40}
    print(pluck(d, "c.e"))

    d = {
        "firstname": "Тимур",
        "lastname": "Гуев",
        "birthdate": {"day": 10, "month": "October", "year": 1993},
        "address": {
            "streetaddress": "Часовая 25, кв. 127",
            "city": {
                "region": "Московская область",
                "type": "город",
                "cityname": "Москва",
            },
            "postalcode": "125315",
        },
    }
    print(pluck(d, "birthdate.weekday", default="Not found"))
