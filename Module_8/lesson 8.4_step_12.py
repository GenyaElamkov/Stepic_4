import functools


class takes_numbers:
    def __init__(self, func) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        if not (
            all(isinstance(arg, (int, float)) for arg in args)
            and all(isinstance(kwarg, (int, float)) for kwarg in kwargs.values())
        ):
            raise TypeError("Аргументы должны принадлежать типам int или float")
        return self.func(*args, **kwargs)


# INPUT DATA:


# TEST_1:
@takes_numbers
def mul(a, b):
    return a * b


print(mul(1, 2))
print(mul(1, 2.5))
print(mul(1.5, 2))
print(mul(1.5, 2.5))


# TEST_2:
@takes_numbers
def mul(a, b):
    return a * b


try:
    print(mul(1, "2"))
except TypeError as error:
    print(error)


# TEST_3:
@takes_numbers
def mul(a, b):
    return a * b


try:
    print(mul("1", 2))
except TypeError as error:
    print(error)


# TEST_4:
@takes_numbers
def mul(a, b):
    return a * b


try:
    print(mul("1", "2"))
except TypeError as error:
    print(error)


# TEST_5:
@takes_numbers
def mul(a, b=2):
    return a * b


try:
    print(mul(1, b="2"))
except TypeError as error:
    print(error)


# TEST_6:
@takes_numbers
def mul(a, b=2):
    """multiplication"""
    return a * b


print(mul.__name__)
print(mul.__doc__)
print(mul(3, 4))

# TEST_7:
print(takes_numbers)


# TEST_8:
@takes_numbers
def mul(a, b=2):
    return a * b


print(mul(1, b=2))


# TEST_9:
@takes_numbers
def mul(a, b):
    return a * b


print(mul(a=1, b=2))
