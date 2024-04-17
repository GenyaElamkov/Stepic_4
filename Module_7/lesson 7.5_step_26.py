from collections.abc import Sequence


class SortedList(Sequence):
    def __init__(self, iterable=[]) -> None:
        self.iterable = sorted(iterable[:])

    def __getitem__(self, index):
        return self.iterable[index]

    def __setitem__(self, index, value):
        raise NotImplementedError

    def __delitem__(self, index):
        del self.iterable[index]

    def __repr__(self) -> str:
        return f"{__class__.__name__}({sorted(self.iterable)})"

    def __len__(self):
        return len(self.iterable)

    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(self.iterable + other.iterable)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, __class__):
            self.iterable += other.iterable
            return self
        return NotImplemented

    def __mul__(self, value):
        if isinstance(value, int):
            return __class__(self.iterable * value)
        return NotImplemented

    def __imul__(self, value):
        if isinstance(value, int):
            self.iterable *= value
            self.iterable.sort()
            return self
        return NotImplemented

    def __reversed__(self):
        raise NotImplementedError

    def add(self, value):
        return self.iterable.append(value)

    def discard(self, value):
        self.iterable = list(filter(lambda x: x != value, self.iterable))

    def update(self, object):
        self.iterable.extend(object)
        self.iterable.sort()

    def append(self, value):
        raise NotImplementedError

    def insert(self, index, value):
        raise NotImplementedError

    def extend(self, object):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError


# INPUT DATA:

# # TEST_1:
# numbers = SortedList([5, 3, 4, 2, 1])


# print(numbers)
# print(numbers[1])
# print(numbers[-2])
# numbers.add(0)
# print(numbers)
# numbers.discard(4)
# print(numbers)
# numbers.update([4, 6])
# print(numbers)

# # TEST_2:
# numbers = SortedList([5, 3, 4, 2, 1])

# print(len(numbers))
# print(*numbers)
# print(1 in numbers)
# print(6 in numbers)

# # TEST_3:
# numbers1 = SortedList([1, 3, 5])
# numbers2 = SortedList([2, 4])

# print(numbers1 + numbers2)
# print(numbers1 * 2)
# print(numbers2 * 2)

# # TEST_4:
# numbers = SortedList([5, 4, 3, 2, 1])

# print(numbers)
# del numbers[1]

# print(numbers)
# del numbers[-1]

# print(numbers)

# try:
#     numbers[0] = 7
# except NotImplementedError:
#     print("Неподдерживаемая операция")

# # TEST_5:
# numbers = SortedList([1, 2, 3, 4, 5])

# try:
#     numbers.append(6)
# except NotImplementedError:
#     print('Неподдерживаемая операция')

# # TEST_6:
# numbers = SortedList([1, 2, 3, 4, 5])

# try:
#     numbers.insert(0, 0)
# except NotImplementedError:
#     print('Неподдерживаемая операция')

# # TEST_7:
# numbers = SortedList([1, 2, 3, 4, 5])

# try:
#     numbers.extend([6, 7, 8, 9, 10])
# except NotImplementedError:
#     print('Неподдерживаемая операция')

# # TEST_8:
# numbers = SortedList([1, 2, 3, 4, 5])

# try:
#     numbers.reverse()
# except NotImplementedError:
#     print('Неподдерживаемая операция')

# # TEST_9:
# numbers = SortedList([1, 2, 3, 4, 5])

# try:
#     reversed(numbers)
# except NotImplementedError:
#     print('Неподдерживаемая операция')

# # TEST_10:
# numbers = SortedList([5, 4, 3, 2, 1])

# numbers.update([5, 4, 3, 2, 1])
# print(*numbers)

# numbers *= 3
# print(*numbers)

# numbers.discard(4)
# print(*numbers)

# # TEST_11:
# numbers1 = SortedList([1, 3, 5])
# numbers2 = SortedList([2, 4])

# id1_numbers1 = id(numbers1)
# id1_numbers2 = id(numbers2)

# numbers1 += numbers2
# numbers2 *= 2

# id2_numbers1 = id(numbers1)
# id2_numbers2 = id(numbers2)

# print(id1_numbers1 == id2_numbers1)
# print(id1_numbers2 == id2_numbers2)
# print(3 in numbers1)

# # TEST_12:
# data = [5, 4, 3, 2, 1]
# numbers = SortedList(data)

# print(numbers)
# data.pop()

# print(data)
# print(numbers)

# # TEST_13:
# numbers = SortedList()
# print(numbers)

# # TEST_14:
# numbers1 = SortedList([5, 3, 4, 2, 1])
# numbers2 = SortedList([10, 9, 8, 7, 6])

# numbers1 = numbers1 + numbers2
# print(numbers1, type(numbers1))

# numbers2 = numbers2 * 2
# print(numbers2, type(numbers2))

# # TEST_15:
# numbers1 = SortedList([5, 3, 4, 2, 1])
# numbers2 = SortedList([10, 9, 8, 7, 6])

# numbers1 += numbers2
# print(numbers1, type(numbers1))

# numbers2 *= 2
# print(numbers2, type(numbers2))

# # TEST_16:
# numbers1 = SortedList([5, 3, 4, 2, 1])
# numbers2 = SortedList([10, 9, 8, 7, 6])

# numbers1 = numbers1 * -100
# print(numbers1)

# numbers2 *= 0
# print(numbers2)

# # TEST_17:
# numbers = SortedList([5, 3, 4, 2, 1])
# print(numbers.__add__(1))
# print(numbers.__iadd__(1.1))
# print(numbers.__mul__([1, 2, 3]))
# print(numbers.__imul__({4, 5, 6}))
