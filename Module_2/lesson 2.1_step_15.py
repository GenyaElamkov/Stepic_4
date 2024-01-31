"""
Функция intersperse()
Реализуйте генераторную функцию intersperse(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
delimiter — значение-разделитель
Функция должна возвращать генератор, порождающий последовательность из элементов итерируемого объекта iterable, между которыми располагается значение-разделитель delimiter.

Примечание 1. Рассмотрим первый тест, в котором в качестве итерируемого объекта передается список чисел от 1 до 3, а в качестве значения-разделителя — 0. Порождаемая генератором последовательность состоит из чисел 1, 2 и 3, между которыми располагается число 0:

1 0 2 0 3

https://stepik.org/lesson/794484/step/15?unit=797232
"""

import itertools

def intersperse(iterable, delimiter):
    """
    >>> print(*intersperse([1, 2, 3], 0))
    1 0 2 0 3
    >>> inter = intersperse('beegeek', '!')
    >>> print(next(inter))
    b
    >>> print(next(inter))
    !
    >>> print(*inter)
    e ! e ! g ! e ! e ! k
    """
    for i, elem in enumerate(iterable):
        if i > 0:
            yield delimiter
        yield elem


# print(intersperse([1, 2, 3], 0))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
