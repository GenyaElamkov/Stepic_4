import itertools


class Peekable:
    def __init__(self, iterable) -> None:
        self.iterable = iter(iterable)
        self.__cnt = 0
        self.__arr = list(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        res = next(self.iterable)
        self.__cnt += 1
        return res

    def peek(self, default=""):
        try:
            return self.__arr[self.__cnt]
        except IndexError:
            if default == "":
                raise StopIteration
            else:
                return default


# SENTINEL = object()

# class Peekable:
#     def __init__(self, iterable):
#         self.iterator = iter(iterable)
#         self.cache = []
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.peek()
#         return self.cache.pop()
    
#     def peek(self, default=SENTINEL):
#         if not self.cache:
#             try:
#                 self.cache.append(next(self.iterator))
#             except StopIteration:
#                 if default is not SENTINEL:
#                     return default
#                 raise
#         return self.cache[0]

# INPUT DATA:

# TEST_1:
iterator = Peekable("beegeek")

print(next(iterator))
print(next(iterator))
print(*iterator)

# TEST_2:
iterator = Peekable("Python")

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())

# TEST_3:
iterator = Peekable("Python")

print(*iterator)
print(iterator.peek(None))

# TEST_4:
iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print("Пустой итератор")

try:
    next(iterator)
except StopIteration:
    print("Пустой итератор")

# TEST_5:
from itertools import islice

iterator = Peekable([n**2 for n in [1, 2, 3, 4, 5]])

print(iterator.peek())
print(list(islice(iterator, 2)))

print(iterator.peek())
print(iterator.peek())

print(list(islice(iterator, 2)))
print(list(islice(iterator, 2)))

# TEST_6:
iterator = Peekable([n**2 for n in [1, 2, 3]])

print(iterator.peek(default=0))
print(*iterator)
print(iterator.peek(default=None))
print(iterator.peek(default=1))
print(iterator.peek(default=[]))
print(iterator.peek(default=()))

# TEST_7:
from itertools import islice

iterator = Peekable([1, 2, 3])

print(iterator.peek())
print(list(islice(iterator, 2)))
print(iterator.peek())
print(list(iterator))

try:
    iterator.peek()
except StopIteration:
    print("Пустой итератор")
