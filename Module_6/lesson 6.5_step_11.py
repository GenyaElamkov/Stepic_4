class Suppress:
    def __init__(self, *args) -> None:
        self.args = args

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type in self.args:
            self.exception = exc_value
            return True

        self.exception = None
        return False



# INPUT DATA:

# TEST_1:
with Suppress(NameError):
    print("Этой переменной не существует -->", variable)

print("Завершение программы")

# TEST_2:
with Suppress(TypeError, ValueError) as context:
    number = int("я число")

print(context.exception)
print(type(context.exception))

# TEST_3:
with Suppress() as context:
    print("All success!")

print(context.exception)

# TEST_4:
with Suppress(ValueError) as context:
    try:
        number = list(123)
    except TypeError:
        pass

print(context.exception)

# TEST_5:
iterable = iter(range(100))

with Suppress(StopIteration) as context:
    for _ in range(99):
        next(iterable)
    print(next(iterable))
    print(next(iterable))


print(context.exception)
print(type(context.exception))

# TEST_6:
d = {"Gvido": 67, "Gates": 67, "Zuckerberg": 38}
with Suppress(KeyError) as context:
    print(d["Mask"])


print(context.exception)
print(type(context.exception))

# TEST_7:
with Suppress(ValueError) as context:
    try:
        print("Несуществующий метод у словаря –>", {}.new())
    except AttributeError as e:
        print(type(e))

print(context.exception)

# TEST_8:
try:
    with Suppress(ValueError) as context:
        number = list(123)
except TypeError:
    pass

print(context.exception)
