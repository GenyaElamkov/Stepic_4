from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register(int)
    @staticmethod
    def _(data):
        print(f"Целое число: {data}")

    @format.register(float)
    @staticmethod
    def _(data):
        print(f"Вещественное число: {data}")

    @format.register(list)
    @staticmethod
    def _(data):

        print(f"Элементы списка: {', '.join(map(repr, data))}")

    @format.register(tuple)
    @staticmethod
    def _(data):
        print(f"Элементы кортежа: {', '.join(map(repr, data))}")

    @format.register(dict)
    @staticmethod
    def _(data):
        res = [f"({repr(k)}, {repr(v)})" for k, v in data.items()]
        print(f"Пары словаря: {', '.join(res)}")


Formatter.format(1337)
Formatter.format(20.77)

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))

Formatter.format({"Cuphead": 1, "Mugman": 3})
Formatter.format({1: "one", 2: "two"})
Formatter.format({1: True, 0: False})

try:
    Formatter.format("All them years, Dutch, for this snake?")
except TypeError as e:
    print(e)
