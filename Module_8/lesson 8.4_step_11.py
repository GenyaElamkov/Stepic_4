import functools


class MaxCallsException(Exception): ...


class limited_calls:
    def __init__(self, n) -> None:
        self.n = n

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwds):
            if self.n == 0:
                raise MaxCallsException("Превышено допустимое количество вызовов")
            value = func(*args, **kwds)
            self.n -= 1
            return value

        return wrapper


# INPUT DATA:


# TEST_1:
@limited_calls(3)
def add(a, b):
    return a + b


print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)

# TEST_2:
import random


@limited_calls(5)
def positive_sum(*args):
    return sum(args)


for _ in range(4):
    positive_sum(*(random.randint(1, 100) for _ in range(10)))

print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

try:
    print(positive_sum(10, 124, 124, 786, 11))
except MaxCallsException as e:
    print(e)


# TEST_3:
@limited_calls(5)
def concat(a, b, c):
    return a + b + c


for _ in range(5):
    print(concat("123", "456", "789"))

try:
    print(concat("123", "456", "789"))
except MaxCallsException as e:
    print(e)


# TEST_4:
@limited_calls(10)
def power(a, n):
    return a**n


for _ in range(10):
    power(2, 3)

try:
    print(power(2, 3))
except MaxCallsException as e:
    print(e)


# TEST_5:
@limited_calls(10)
def power(a, n):
    """degree"""
    return a**n


print(power.__name__)
print(power.__doc__)
print(power(2, 3))
