from functools import wraps
from typing import Any

# def counter(n: int):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 val = func(*args, **kwargs)
#             return val
#         return wrapper
#     return decorator

# class Cat:
#     def __init__(self, name) -> None:
#         self.name = name
    
#     @counter(10)
#     def go_home(self):
#         print(self.name)


# cat = Cat('Kitte')
# cat.go_home()


class Cat:
    def __init__(self, func, n) -> None:
        self.func = func
        self.n = n


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for _ in range(self.n):
            val = self.func(*args, **kwds)
        return val

def cat(name):
    print(name)


cats =  Cat(cat, 10)
cats('Kitty')