from collections.abc import Sequence


class CustomRange(Sequence):
    def __init__(self, *args) -> None:
        arr = []
        for elem in args:
            if isinstance(elem, str):
                start, end = map(int, elem.split("-"))
                arr.extend(range(start, end + 1))
            else:
                arr.append(elem)
        self._args = arr

    def __getitem__(self, index):
        return self._args[index]

    def __len__(self):
        return len(self._args)

    def __reversed__(self):
        return self._args[::-1]


# INPUT DATA:

# TEST_1:
customrange = CustomRange(1, "2-5", 5, "6-8")

print(customrange[0])
print(customrange[1])
print(customrange[2])
print(customrange[-1])
print(customrange[-2])
print(customrange[-3])

# TEST_2:
customrange = CustomRange(1, "2-5", 3, "1-4")

print(*customrange)
print(*reversed(customrange))
print(len(customrange))
print(1 in customrange)
print(10 in customrange)

# TEST_3:
customrange = CustomRange()

print(len(customrange))
print(*customrange)
print(*reversed(customrange))

# TEST_4:
customrange = CustomRange("0-1000")

print(len(customrange))
print(*customrange)

# TEST_5:
customrange = CustomRange("0-50", "25-75", "50-100")

for digit in customrange:
    print(digit, end=" ")

# TEST_6:
customrange = CustomRange(1, 212, "89-323", 87, "17-82", 124, "300-312", 832, 1234)

print(*customrange)
print(customrange[11])
print(customrange[44])
print(customrange[-12])
print(customrange[-38])
print(82 in customrange)
print(17 in customrange)
