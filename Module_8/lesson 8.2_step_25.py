from datetime import date, timedelta
from enum import IntEnum


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    def __init__(
        self, today: date, weekday: Weekday, after_today: bool = False
    ) -> None:
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        self.cnt = 0 if self.after_today else 1
        while True:
            res = self.today + timedelta(days=self.cnt)
            if res.weekday() == self.weekday.value:
                return res
            self.cnt += 1

    def days_until(self):
        return self.cnt


# Weekday = IntEnum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


# class NextDate:
#     def __init__(self, today, weekday, after_today=False):
#         self.today = today
#         self.weekday = weekday
#         self.after_today = after_today

#     def date(self):
#         next_date = self.today + timedelta((self.weekday - self.today.weekday()) % 7)
#         if not self.after_today and next_date == self.today:
#             next_date += timedelta(7)
#         return next_date

#     def days_until(self):
#         return (self.date() - self.today).days


# INPUT DATA:

# # TEST_1:
# from datetime import date

# today = date(2023, 4, 17)  # понедельник
# next_friday = NextDate(today, Weekday.FRIDAY)  # следующая пятница

# print(next_friday.date())
# print(next_friday.days_until())

# # TEST_2:
# from datetime import date

# today = date(2023, 4, 17)  # понедельник
# next_monday = NextDate(
#     today, Weekday.MONDAY
# )  # следующий понедельник без учета текущего

# print(next_monday.date())
# print(next_monday.days_until())

# # TEST_3:
# from datetime import date

# today = date(2023, 4, 17)  # понедельник
# next_monday = NextDate(
#     today, Weekday.MONDAY, True
# )  # следующий понедельник с учетом текущего

# print(next_monday.date())
# print(next_monday.days_until())

# # TEST_4:
# from datetime import date

# for weekday in Weekday:
#     today = date(2023, 4, 27)  # четверг
#     next_date = NextDate(today, weekday)

#     print(next_date.date())
#     print(next_date.days_until())

# # TEST_5:
# from datetime import date

# for weekday in Weekday:
#     today = date(2023, 4, 27)  # четверг
#     next_date = NextDate(today, weekday, True)

#     print(next_date.date())
#     print(next_date.days_until())

# # TEST_6:
# from datetime import date, timedelta

# today = date(2023, 4, 23)

# for _ in range(7):
#     today += timedelta(days=1)
#     for weekday in Weekday:
#         next_date = NextDate(today, weekday)
#         print(
#             f"Today = {today} {Weekday(today.weekday()).name}, next {weekday.name} = {next_date.date()}"
#         )
#         print(f"Days until = {next_date.days_until()}")

# TEST_7:
from datetime import date, timedelta

today = date(2023, 4, 23)

for _ in range(7):
    today += timedelta(days=1)
    for weekday in Weekday:
        next_date = NextDate(today, weekday, True)
        print(
            f"Today = {today} {Weekday(today.weekday()).name}, next {weekday.name} = {next_date.date()}"
        )
        print(f"Days until = {next_date.days_until()}")
