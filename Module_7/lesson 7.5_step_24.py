from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=[]) -> None:
        self.iterable = iterable[:]

    def __str__(self):
        return f"{self.iterable}"

    def __getitem__(self, index):
        return self.iterable[index]

    def __len__(self):
        return len(self.iterable)

    def __invert__(self):
        return __class__([int(not i) for i in self.iterable])

    def __or__(self, other):
        if not isinstance(other, Sequence) or len(self) != len(other):
            return NotImplemented
        return __class__([a | b for a, b in zip(self, other)])

    def __and__(self, other):
        if not isinstance(other, Sequence) or len(self) != len(other):
            return NotImplemented
        return __class__([a & b for a, b in zip(self, other)])


# # INPUT DATA:

# # TEST_1:
# bitarray = BitArray([1, 0, 1, 1])

# print(bitarray)
# print(~bitarray)
# print(bitarray[0])
# print(bitarray[1])
# print(bitarray[-1])
# print(0 in bitarray)
# print(1 not in bitarray)

# # TEST_2:
# bitarray1 = BitArray([1, 0, 1, 1])
# bitarray2 = BitArray([0, 0, 0, 1])

# bitarray3 = bitarray1 | bitarray2
# bitarray4 = bitarray1 & bitarray2
# bitarray5 = ~bitarray1

# print(bitarray3, type(bitarray3))
# print(bitarray4, type(bitarray4))
# print(bitarray5, type(bitarray5))

# # TEST_3:
# data = [
#     1,
#     0,
#     1,
#     0,
#     1,
#     0,
#     0,
#     1,
#     0,
#     0,
#     0,
#     0,
#     0,
#     1,
#     1,
#     1,
#     1,
#     1,
#     0,
#     0,
#     1,
#     0,
#     0,
#     1,
#     1,
#     0,
#     0,
#     1,
#     0,
#     0,
#     1,
#     0,
#     0,
#     0,
#     1,
#     0,
#     1,
#     1,
#     0,
#     0,
#     0,
#     1,
#     0,
#     0,
#     0,
#     0,
#     1,
#     1,
#     1,
#     0,
# ]

# bitarray = BitArray(data)

# print(*bitarray)
# print(*reversed(bitarray))
# print(~bitarray)

# TEST_4:
data = [
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0,
]

bitarray = BitArray(data)

print(bitarray)
data.extend([0, 0, 1, 0, 1, 1])

print(data)
print(bitarray)

# # TEST_5:
# data1 = [
#     0,
#     1,
#     1,
#     0,
#     0,
#     1,
#     0,
#     0,
#     1,
#     1,
#     0,
#     1,
#     0,
#     0,
#     0,
#     1,
#     1,
#     0,
#     0,
#     1,
#     1,
#     1,
#     1,
#     0,
#     1,
#     1,
#     1,
#     0,
#     1,
#     0,
#     1,
#     1,
#     1,
#     0,
#     0,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     0,
#     0,
#     0,
#     0,
#     1,
#     1,
#     0,
# ]

# data2 = [
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     0,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     0,
#     1,
#     0,
#     0,
#     0,
#     0,
#     0,
#     1,
#     0,
#     1,
#     1,
#     1,
#     0,
#     0,
#     1,
#     0,
#     1,
#     0,
#     1,
#     0,
#     1,
#     1,
#     1,
#     1,
#     1,
#     0,
#     0,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     0,
#     0,
#     1,
# ]

# bitarray1 = BitArray(data1)
# bitarray2 = BitArray(data2)


# print(len(bitarray1) == len(bitarray2))
# print(bitarray1 | bitarray2)
# print(bitarray1 & bitarray2)

# # TEST_6:
# bitarray = BitArray([1, 0, 1, 1])
# print(bitarray.__or__(1))
# print(bitarray.__and__(1.1))

# # TEST_7:
# bitarray = BitArray()
# print(bitarray)

# # TEST_8:
# data1 = [0, 1, 1, 0, 0, 1]
# data2 = [1, 1, 1, 1, 1]

# bitarray1 = BitArray(data1)
# bitarray2 = BitArray(data2)

# try:
#     print(bitarray1 | bitarray2)
# except TypeError:
#     print("Списки должны быть равной длины")

# try:
#     print(bitarray1 & bitarray2)
# except TypeError:
#     print("Списки должны быть равной длины")
