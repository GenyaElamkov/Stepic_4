"""
Функция is_fraction()
Будем считать обыкновенной дробью последовательность из одной или более цифр, за которой следует прямая косая черта /, а затем — последовательность из одной или более цифр, хотя бы одна из которых отлична от нуля (знаменатель не может равняться нулю). Последовательность, представляющая собой обыкновенную дробь, может начинаться с необязательного символа дефиса -.

Реализуйте функцию is_fraction(), которая принимает один аргумент:

string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой обыкновенную дробь, или False в противном случае.


https://stepik.org/lesson/794484/step/14?unit=797232
"""

import re

def is_fraction(string: str) -> bool:
    """
    >>> print(is_fraction('1000/1'))
    True
    >>> print(is_fraction('-54/9'))
    True
    >>> print(is_fraction('71'))
    False
    >>> print(is_fraction('1 / 82'))
    False
    >>> print(is_fraction('1/0'))
    False
    >>> print(is_fraction('5/8-'))
    False
    >>> print(is_fraction('1000/00004123'))
    True
    >>> print(is_fraction('1000/0000'))
    False
    >>> print(is_fraction('1000/00000008000'))
    True
    """
    match = re.fullmatch(r"^-?(\d+)\/(\d+)", string)
    try:
        if int(match.group(2)) == 0:
            return False
        return True
    except AttributeError:
        return False
    


if __name__ == "__main__":
    import doctest

    doctest.testmod()
