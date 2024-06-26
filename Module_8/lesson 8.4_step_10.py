import functools


class reverse_args:
    def __init__(self, func) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwds):
        args = reversed(args)
        return self.func(*args, **kwds)


# INPUT DATA:


# TEST_1:
@reverse_args
def power(a, n):
    return a**n


print(power(2, 3))


# TEST_2:
@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat("apple", "cherry", "melon"))


# TEST_3:
@reverse_args
def operation(a, b, c):
    return a // b + c


print(operation(10, 20, 80))


# TEST_4:
@reverse_args
def operation(a, b):
    """integer division"""
    return a // b


print(operation.__name__)
print(operation.__doc__)
print(operation(90, 0))


# TEST_5:
@reverse_args
def operation(a, b):
    return a // b


try:
    print(operation(0, 70))
except ZeroDivisionError:
    print("ZeroDivisionError")


# TEST_6:
@reverse_args
def operation(a, b, name):
    return a // b + name


print(operation(10, 90, name=1))


# TEST_7:
@reverse_args
def operation(a, b, value=10):
    return a // b + value


try:
    print(operation(0, 70))
except ZeroDivisionError:
    print("ZeroDivisionError")


# TEST_8:
@reverse_args
def operation(a, b, value1=10, value2=30):
    return a // b - value1 + value2


print(operation(140, 70, value1=50, value2=100))

# TEST_9:
print(reverse_args)
print(type(reverse_args))
