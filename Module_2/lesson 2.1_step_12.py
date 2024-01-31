"""
Функция is_integer()
Целым числом будем считать последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -.

Реализуйте функцию is_integer(), которая принимает один аргумент:

string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой целое число, или False в противном случае.


https://stepik.org/lesson/794484/step/12?unit=797232
"""
import re

def is_integer(string: str):
    # match = re.search(r"^-?(.+)", string).group(1)
    # return match.isdigit()
    return re.fullmatch(r"^-?\d+", string)



print(is_integer('199'))