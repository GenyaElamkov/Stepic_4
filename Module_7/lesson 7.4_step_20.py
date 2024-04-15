from collections import UserList


class NumberList(UserList):

    def __init__(self, iterable):
        [self.check(elem) for elem in iterable]
        super().__init__(iterable)

    def check(self, item):
        if isinstance(item, (int, float)):
            return item
        raise TypeError("Элементами экземпляра класса NumberList должны быть числа")

    def __setitem__(self, index, item):
        self.check(self.data[index])
        self.data[index] = self.check(item)

    def insert(self, index, item):
        self.check(item=item)
        return super().insert(index, item)

    def append(self, item):
        self.check(item=item)
        return super().append(item)

    def extend(self, other) -> None:
        for elem in other:
            self.check(item=elem)
        return super().extend(other)

    def __iadd__(self, other):
        for elem in other:
            self.check(item=elem)
        return super().__iadd__(other)


# INPUT DATA:

# TEST_1:
numberlist = NumberList([1, 2])

numberlist.append(3)
numberlist.extend([4, 5])
numberlist.insert(0, 0)
print(numberlist)

# TEST_2:
numberlist = NumberList([0, 1.0])

numberlist[1] = 1
numberlist = numberlist + NumberList([2, 3])
numberlist += NumberList([4, 5])
print(numberlist)

# TEST_3:
try:
    numberlist = NumberList(["a", "b", "c"])
except TypeError as error:
    print(error)

# TEST_4:
numberlist = NumberList([1, 2, 3])

try:
    numberlist.append("4")
except TypeError as error:
    print(error)

# TEST_5:
numberlist = NumberList([1, 2])

try:
    numberlist += [3, "4"]
except TypeError as e:
    print(e)

# TEST_6:
numberlist1 = NumberList([1, 2])

try:
    numberlist2 = numberlist1 + [3, "4"]
except TypeError as e:
    print(e)

# TEST_7:
data = [1, 2, 3]
numberlist = NumberList(data)

print(numberlist)

data.extend([4, 5, 6])
print(data)
print(numberlist)

# TEST_8:
numberlist = NumberList([1, 2])
try:
    numberlist.insert(0, [5, 4, 3])
except TypeError as e:
    print(e)

# TEST_9:
numberlist = NumberList([1, 2])
try:
    numberlist.extend([5, "4", 3])
except TypeError as e:
    print(e)

# TEST_10:
n = NumberList([1, 2, 3])

try:
    n[1] = "5"
except TypeError as e:
    print(e)
