"""
Декоратор @jsonify
Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемое значение функции принадлежит типу, который поддерживается форматом JSON.

https://stepik.org/lesson/794484/step/8?unit=797232
"""

import functools
import json


def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return json.dumps(value)

    return wrapper


@jsonify
def make_list(n):
    return list(range(1, n + 1))


print(make_list(10))
