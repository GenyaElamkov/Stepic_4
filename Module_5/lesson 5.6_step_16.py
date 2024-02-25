class CountCalls:
    def __init__(self, func) -> None:
        self.func = func
        self.__calls = 0

    @property
    def calls(self):
        return self.__calls

    def __call__(self, *args, **kwargs):
        self.__calls += 1
        return self.func(*args, **kwargs)


@CountCalls
def add(a, b):
    return a + b


print(add(1, 2))
print(add(2, 3))
print(add.calls)
