"""
Функция is_decimal()
Будем считать вещественным числом последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -, а также содержать на любой позиции одну десятичную точку ., кроме случая, когда точка стоит перед символом дефиса.

Реализуйте функцию is_decimal(), которая принимает один аргумент:

string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой целое или вещественное число, или False в противном случае.


https://stepik.org/lesson/794484/step/13?unit=797232
"""


def is_decimal(string: str) -> bool:
    """
    >>> print(is_decimal('100'))
    True
    >>> print(is_decimal('199.1'))
    True
    >>> print(is_decimal('-0.2'))
    True
    >>> print(is_decimal('.-95'))
    False
    >>> print(is_decimal('-.95'))
    True
    >>> print(is_decimal('.10'))
    True
    >>> strings = ['100.', '349..', '-425.', '-1248..']
    """
    try:
        return bool(float(string))
    except ValueError:
        return False
    
    
if __name__ == "__main__":
    import doctest

    doctest.testmod()
