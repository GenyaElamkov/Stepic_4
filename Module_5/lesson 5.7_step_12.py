from functools import total_ordering
from math import floor


@total_ordering
class RomanNumeral:
    d = {"m": 1000, "d": 500, "c": 100, "l": 50, "x": 10, "v": 5, "i": 1}
    d_revers = {v: k for k, v in d.items()}

    def __init__(self, number) -> None:
        self.number = number

    def __str__(self) -> str:
        return f"{self.number}"

    def __int__(self):
        return int(self.to_arab(self.number))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, __class__):
            return self.number == other.number
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, __class__):
            return self.number <= other.number
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, __class__):
            res = self.to_arab(self.number) + other.to_arab(other.number)
            return __class__(self.to_roman(res))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, __class__):
            res = self.to_arab(self.number) - other.to_arab(other.number)
            return __class__(self.to_roman(res))
        return NotImplemented

    @classmethod
    def to_arab(cls, roman: str) -> int:
        num = [__class__.d[i] for i in roman.lower() if i in __class__.d]
        nums = []
        for i, val in enumerate(num):
            if val >= num[min(i + 1, len(num) - 1)]:
                nums.append(val)
            else:
                nums.append(-val)
        return int(sum(nums))

    @classmethod
    def to_roman(cla, num: int) -> str:
        div = 1
        while num >= div:
            div *= 10

        div /= 10
        res = ""

        while num:
            last_num = int(num / div)
            if last_num <= 3:
                res += __class__.d_revers[div] * last_num
            elif last_num == 4:
                res += __class__.d_revers[div] + __class__.d_revers[div * 5]
            elif 5 <= last_num <= 8:
                res += __class__.d_revers[div * 5] + (
                    __class__.d_revers[div] * (last_num - 5)
                )
            elif last_num == 9:
                res += __class__.d_revers[div] + __class__.d_revers[div * 10]

            num = floor(num % div)
            div /= 10
        return res.upper()


# INPUT DATA:

# TEST_1:
number = RomanNumeral("IV") + RomanNumeral("VIII")

print(number)
print(int(number))

# TEST_2:
number = RomanNumeral("X") - RomanNumeral("VI")

print(number)
print(int(number))

# TEST_3:
a = RomanNumeral("X")
b = RomanNumeral("XII")

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_4:
a = RomanNumeral("X")
b = RomanNumeral("X")

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_5:
number = RomanNumeral("MXL") + RomanNumeral("MCDVIII") - RomanNumeral("I")

print(number)
print(int(number))

# TEST_6:
number = (
    RomanNumeral("I") + RomanNumeral("II") + RomanNumeral("III") - RomanNumeral("V")
)

print(number)
print(int(number))

# TEST_7:
romans1 = ["I", "X", "L", "IV", "IX", "XLV", "CXXIV", "MCMXCIV"]
romans2 = ["I", "V", "L", "VI", "XI", "XXV", "CDXLVIII", "MCMXCI"]

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) + RomanNumeral(y)
    print(number, int(number))

# TEST_8:
romans1 = ["III", "X", "L", "C", "M", "XXV", "XC", "MMMCMXXXV"]
romans2 = ["II", "V", "X", "L", "D", "IV", "VIII", "MCMXCIV"]

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) - RomanNumeral(y)
    print(number, int(number))

# TEST_9:
romans = ["I", "IV", "IX", "XII", "XXV", "XLV", "LXIX", "XC", "CDXLVIII"]

for num in romans:
    print(RomanNumeral(num), int(RomanNumeral(num)))

# TEST_10:
roman = RomanNumeral("L")
print(roman.__eq__(1))
print(roman.__ne__(1.1))
print(roman.__gt__(range(5)))
print(roman.__lt__([1, 2, 3]))
print(roman.__ge__({4, 5, 6}))
print(roman.__le__({1: "one"}))
