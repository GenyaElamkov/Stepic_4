class CachedFunction:
    def __init__(self, func) -> None:
        self.func = func
        self.__cache = {}

    @property
    def cache(self):
        return self.__cache

    def __call__(self, *args, **kwargs):
        result = self.__cache.get(args)
        if args not in self.__cache:
            result = self.func(*args, **kwargs)
            self.__cache[args] = result
        return result


@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


print(slow_fibonacci(100))
