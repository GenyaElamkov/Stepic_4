class ModularTuple(tuple):
    def __new__(cls, iterable=(), size: int = 100, *args, **kwargs):
        res = [i % size for i in iterable]
        return super().__new__(cls, res)


# INPUT DATA:

# TEST_1:
modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))

# TEST_2:
modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)

print(modulartuple)

# TEST_3:
modulartuple = ModularTuple()
print(modulartuple)

# TEST_4:
modulartuple = ModularTuple([1, 2, 3, 4, 5], 1)

print(modulartuple)

# TEST_5:
data = [1, 2, 3, 4, 5]
modulartuple = ModularTuple(data, -5)

print(modulartuple)

data.extend([6, 7, 8, 9, 10])
print(data)
print(modulartuple)
