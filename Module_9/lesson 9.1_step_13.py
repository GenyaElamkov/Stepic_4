"""
Класс predicate в вашем коде представляет собой декоратор класса, который 
позволяет создавать пользовательские логические функции. 
Вот краткое объяснение того, что делает каждая метод класса:

__init__(self, func) -> None: Этот метод инициализирует объект predicate с функцией func. 
Он использует functools.update_wrapper, чтобы обновить атрибуты объекта predicate, 
чтобы они соответствовали атрибутам func.

__call__(self, *args, **kwds): Этот метод позволяет вызывать объект класса predicate 
как функцию. Он просто вызывает функцию func с предоставленными аргументами и 
ключевыми аргументами.

__invert__(self): Этот метод возвращает новый объект класса predicate, который 
представляет логическое отрицание исходного объекта predicate. Он делает это, 
создавая новую лямбда-функцию, которая возвращает логическое НЕ результата вызова
 исходной функции.

__or__(self, other): Этот метод возвращает новый объект класса predicate, который 
представляет логическое ОР исходного объекта predicate и объекта other. Он делает 
это, создавая новую лямбда-функцию, которая возвращает логическое ОР результатов
 вызова исходной функции и функции other.

__and__(self, other): Этот метод возвращает новый объект класса predicate, который 
представляет логическое ИСКЛЮЧАЮЩЕ исходного объекта predicate и объекта other. 
Он делает это, создавая новую лямбда-функцию, которая возвращает логическое 
ИСКЛЮЧАЮЩЕ результатов вызова исходной функции и функции other.
Эти методы позволяют вам создавать пользовательские логические функции, которые 
могут использоваться в условных конструкциях и других логических операциях, 
похожих на работу встроенных логических функций Python.
"""


import functools


class predicate:
    def __init__(self, func) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwds):
        return self.func(*args, **kwds)

    def __invert__(self):
        return __class__(lambda *args, **kwds: not self(*args, **kwds))

    def __or__(self, other):
        return __class__(
            lambda *args, **kwds: self(*args, **kwds) or other(*args, **kwds)
        )

    def __and__(self, other):
        return __class__(
            lambda *args, **kwds: self(*args, **kwds) and other(*args, **kwds)
        )


# # INPUT DATA:


# # TEST_1:
# @predicate
# def to_be():
#     return True


# print((to_be | ~to_be)())  # True; равнозначно to_be() or not to_be()


# @predicate
# def is_equal(a, b):
#     return a == b


# @predicate
# def is_less_than(a, b):
#     return a < b


# print(
#     (is_less_than | is_equal)(1, 2)
# )  # True; равнозначно is_less_than(1, 2) or is_equal(1, 2)

# print(
#     (is_less_than | is_equal)(2, b=2)
# )  # True; равнозначно is_less_than(2, b=2) or is_equal(2, b=2)
# print(
#     (is_less_than | is_equal)(a=3, b=2)
# )  # False; равнозначно is_less_than(a=3, b=2) or is_equal(a=3, b=2)

# # TEST_2:
# @predicate
# def is_even(num):
#     return num % 2 == 0

# @predicate
# def is_positive(num):
#     return num > 0

# print((is_even & is_positive)(4))             # True; равнозначно is_even(4) and is_positive(4)
# print((is_even & is_positive)(3))             # False; равнозначно is_even(3) and is_positive(3)
# print((is_even | is_positive)(3))             # True; равнозначно is_even(3) or is_positive(3)
# print((~is_even & is_positive)(3))            # True; равнозначно not is_even(3) and is_positive(3)

# # TEST_3:
# @predicate
# def is_less_than(a, b):
#     return a < b

# print(is_less_than(1, 2))
# print(is_less_than(2, 2))
# print(is_less_than(3, 2))

# # TEST_4:
# @predicate
# def char_in_word(char, word):
#     return char in word


# print(char_in_word('e', 'beegeek'))
# print((~char_in_word & char_in_word)('e', 'beegeek'))
# print((char_in_word | ~char_in_word)(word='beegeek', char='e'))


# TEST_5:
@predicate
def is_arithmetic_mean(iterable):
    result = {iterable[i + 1] - iterable[i] for i in range(len(iterable) - 1)}
    return len(result) == 1


@predicate
def is_geometric_mean(iterable):
    result = {iterable[i + 1] // iterable[i] for i in range(len(iterable) - 1)}
    return len(result) == 1


print(is_arithmetic_mean([1, 2, 3, 4, 5]))
print(is_geometric_mean([1, 2, 4, 8, 16]))

print((is_arithmetic_mean & is_geometric_mean)([1, 2, 3, 4, 5]))
print((is_arithmetic_mean | is_geometric_mean)([1, 2, 3, 4, 5]))

print((is_arithmetic_mean & is_geometric_mean)([1, 2, 4, 8, 16]))
print((is_arithmetic_mean | is_geometric_mean)([1, 2, 4, 8, 16]))

print((~is_arithmetic_mean & ~is_geometric_mean)([1, 2, 4, 5]))
print((~is_arithmetic_mean | ~is_geometric_mean)([1, 2, 3, 4, 5]))
