from abc import ABC, abstractmethod


class Stats(ABC):
    def __init__(self, iterable: list = []) -> None:
        self.iterable = iterable

    def add(self, n: int):
        self.iterable.append(n)

    @abstractmethod
    def result(self):
        raise NotADirectoryError

    def clear(self):
        self.iterable.clear()


class MinStat(Stats):
    def result(self):
        return min(self.iterable, default=None)


class MaxStat(Stats):
    def result(self):
        return max(self.iterable, default=None)


class AverageStat(Stats):
    def result(self):
        if not self.iterable:
            return None
        return sum(self.iterable) / len(self.iterable)


minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
