import functools


class exception_decorator:
    def __init__(self, func) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs), None
        except Exception as exp:
            return None, type(exp)


# INPUT DATA:


# TEST_1:
@exception_decorator
def func(x):
    return 2 * x + 1


print(func(1))
print(func("bee"))


# TEST_2:
@exception_decorator
def f(x, y):
    return x * y


print(f("stepik", 10))


# TEST_3:
@exception_decorator
def f(x, y):
    return x * y


print(f("stepik", "stepik"))


# TEST_4:
@exception_decorator
def f(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(f(1, 2, 3, param1=4, param2=10))


# TEST_5:
@exception_decorator
def f(*args, **kwargs):
    """sum args and kwargs"""
    return sum(args) + sum(kwargs.values())


print(f.__name__)
print(f.__doc__)
print(f(1, 2, 3, param1=4, param2="10"))

# TEST_6:
sum = exception_decorator(sum)

print(sum(["199", "1", 187]))
