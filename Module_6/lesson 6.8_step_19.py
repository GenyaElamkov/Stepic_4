from random import randint


class RandomNumber:
    def __init__(self, start: int, end: int, cache: bool = False) -> None:
        self._start = start
        self._end = end
        self._cache = cache
        self._rand = randint(start, end)

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        return self._rand

    def __set__(self, obj, value):
        raise AttributeError("Изменение невозможно")


# import random


# class RandomNumber:
#     def __init__(self, start, end, cache=False):
#         self.start = start
#         self.end = end
#         self.cache = cache

#     def __set_name__(self, cls, attr):
#         self._attr = attr

#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self.cache and self._attr in obj.__dict__:
#             return obj.__dict__[self._attr]
#         number = random.randint(self.start, self.end)
#         if self.cache:
#             obj.__dict__[self._attr] = number
#         return number

#     def __set__(self, obj, value):
#         raise AttributeError('Изменение невозможно')


# INPUT DATA:


# TEST_1:
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)


magicpoint = MagicPoint()

print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])


# TEST_2:
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)


magicpoint = MagicPoint()

print(magicpoint.x in [6, 7, 8, 9, 10])
print(magicpoint.y in [6, 7, 8, 9, 10])
print(magicpoint.z in [6, 7, 8, 9, 10])


# TEST_3:
class MagicPoint:
    x = RandomNumber(0, 5, True)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)


magicpoint = MagicPoint()
value = magicpoint.x

print(magicpoint.x in [0, 1, 2, 3, 4, 5])
print(magicpoint.x == value)
print(magicpoint.x == value)
print(magicpoint.x == value)


# TEST_4:
class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)


magicpoint = MagicPoint()

try:
    magicpoint.x = 10
except AttributeError as e:
    print(e)


# TEST_5:
class MagicPoint:
    x = RandomNumber(20, 100, True)


magicpoint = MagicPoint()

value = magicpoint.x

for _ in range(20):
    print(magicpoint.x == value)


# TEST_6:
class MagicPoint:
    x = RandomNumber(-1000, 1000)


magicpoint = MagicPoint()

for _ in range(50):
    print(magicpoint.x in range(-1000, 1001))


# TEST_7:
class MagicPoint:
    x = RandomNumber(-1000, 1000)

    def __init__(self, x):
        self.x = x


try:
    magicpoint = MagicPoint(150)
except AttributeError as e:
    print(e)


# TEST_8:
class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)


print(MagicPoint.x.__class__)
print(MagicPoint.y.__class__)
print(MagicPoint.z.__class__)
