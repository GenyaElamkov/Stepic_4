import re

from datetime import date
from functools import singledispatchmethod


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date) -> None | TypeError:
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register(date)
    def _(self, birth_date) -> None:
        self.birth_date = birth_date

    @__init__.register(str)
    def _(self, birth_date: str) -> None | TypeError:
        match = re.findall(r"^\d{4}-\d{2}-\d{2}$", birth_date)
        if not match:
            raise TypeError("Аргумент переданного типа не поддерживается")
        self.birth_date = date(*map(int, birth_date.split("-")))

    @__init__.register(tuple)
    @__init__.register(list)
    def _(self, birth_date) -> None:
        self.birth_date = date(*birth_date)

    @property
    def age(self) -> int:
        today = date.today()
        return (
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )


birthinfo1 = BirthInfo("2020-09-18")
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)

# errors = [20200918, True, {1: 'one'}, {1, 2, 3}, 100.9]

# for obj in errors:
#     try:
#         BirthInfo(obj)
#     except TypeError as e:
#         print(e)

# birth_dates = ["20200918", "2020-0918", "202009-18", " 2020-09-18 ", "2020-9-18"]

# for birth_date in birth_dates:
#     try:
#         birthinfo1 = BirthInfo(birth_date)
#     except TypeError as e:
#         print(e)
