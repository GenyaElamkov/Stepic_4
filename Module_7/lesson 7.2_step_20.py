class Summator:
    def __init__(self) -> None:
        self._m = 1

    def total(self, n: int):
        return sum(pow(i, self._m) for i in range(1, n + 1))


class SquareSummator(Summator):
    def __init__(self) -> None:
        self._m = 2

    def total(self, n: int):
        return super().total(n)


class QubeSummator(Summator):
    def __init__(self) -> None:
        self._m = 3

    def total(self, n: int):
        return super().total(n)


class CustomSummator(Summator):
    def __init__(self, m) -> None:
        self._m = m

    def total(self, n: int):
        return super().total(n)


# INPUT DATA:

# TEST_1:
print(issubclass(SquareSummator, Summator))
print(issubclass(QubeSummator, Summator))

# TEST_2:
summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))  # 1 + 2 + 3
print(summator2.total(3))  # 1 + 4 + 9
print(summator3.total(3))  # 1 + 8 + 27

# TEST_3:
summator1 = Summator()
summator2 = CustomSummator(2)
summator3 = CustomSummator(3)

print(summator1.total(3))  # 1 + 2 + 3
print(summator2.total(3))  # 1 + 4 + 9
print(summator3.total(3))  # 1 + 8 + 27

# TEST_4:
summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

for i in range(5, 50):
    print(summator1.total(i), summator2.total(i), summator3.total(i))

# TEST_5:
for i in range(5, 50):
    summator = CustomSummator(i)
    print(summator.total(10))
