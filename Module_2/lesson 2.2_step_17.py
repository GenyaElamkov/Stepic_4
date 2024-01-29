"""
Функция pluck()
Реализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:

data — словарь произвольной вложенности
path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно
Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность ключей, например, key1.key2, то возвращаемым значением функции должно быть значение по ключу key2 из словаря data[key1]. Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет, функция должна вернуть значение default.

https://stepik.org/lesson/794484/step/17?unit=797232
"""


def pluck(data: dict, path: str, default=None):
    # if path in data:
    #     return data[path]

    # for val in data.values():
    #     if isinstance(val, dict):
    #         val = pluck(val, path)
    #     if val is not None:
    #         return val

    for k in path.split('.'):
        if isinstance(data[k], dict):
            return pluck(data[k], k)
        return data[k]
    






if __name__ == "__main__":
    d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
    print(pluck(d, 'x'))

    d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
    print(pluck(d, 'a.b'))

    d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

    print(pluck(d, 'a.b.c'))