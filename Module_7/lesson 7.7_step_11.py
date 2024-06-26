from abc import ABC, abstractmethod
from datetime import datetime


class Dates(ABC):
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day
        self._date = datetime(self.year, self.month, self.day)

    @abstractmethod
    def format(self):
        pass

    def iso_format(self):
        return self._date.strftime("%Y-%m-%d")


class USADate(Dates):
    def format(self):
        return self._date.strftime("%m-%d-%Y")

class ItalianDate(Dates):
    def format(self):
        return self._date.strftime("%d/%m/%Y")


# INPUT DATA:

# TEST_1:
usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())

# TEST_2:
italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())

# TEST_3:
dates = [(1960, 8, 3), (2009, 9, 15), (2017, 5, 21), (2020, 5, 8), (1974, 11, 19), (1992, 10, 1), (1998, 9, 9),
         (1991, 12, 18), (1987, 2, 16), (1992, 4, 7), (1975, 12, 15), (1997, 1, 1), (2016, 6, 4), (2002, 6, 18),
         (1973, 1, 21), (2004, 8, 7), (1995, 4, 15), (1995, 10, 22), (1969, 12, 26), (1970, 7, 9), (1978, 4, 3),
         (1979, 4, 10), (1966, 3, 21), (1966, 6, 10), (1973, 6, 22), (1982, 4, 18), (1972, 12, 1), (2010, 3, 2),
         (1962, 3, 17), (2014, 6, 28), (1963, 3, 10), (1971, 3, 5), (1960, 6, 10), (2019, 1, 11), (2005, 10, 15),
         (1981, 1, 19), (2008, 11, 23), (2009, 3, 7), (1963, 7, 16), (2003, 11, 6), (2022, 6, 13), (1975, 12, 10),
         (1979, 9, 14), (2016, 10, 24), (2007, 3, 11), (1962, 10, 28), (2001, 5, 21), (2010, 1, 11), (1990, 12, 18),
         (2010, 5, 25)]

for year, day, month in dates:
    usadate = USADate(year, day, month)
    print(usadate.format(), usadate.iso_format())

# TEST_4:
dates = [(1988, 2, 28), (2006, 8, 26), (2010, 11, 22), (2021, 9, 13), (1967, 8, 26), (1964, 1, 22), (1983, 12, 7),
         (1967, 11, 5), (1971, 4, 3), (1971, 6, 4), (1986, 9, 14), (2014, 5, 8), (2000, 2, 22), (2005, 7, 5),
         (2018, 5, 10), (1988, 12, 17), (2006, 3, 8), (1993, 9, 4), (1995, 1, 13), (2013, 4, 10), (1998, 12, 25),
         (1996, 4, 23), (1987, 7, 27), (2011, 4, 14), (1970, 2, 11), (1970, 8, 18), (1978, 8, 13), (2000, 8, 22),
         (1982, 1, 13), (1990, 12, 5), (1984, 7, 14), (1987, 3, 28), (1962, 9, 1), (2015, 9, 26), (2020, 12, 10),
         (2008, 11, 1), (1967, 1, 23), (1994, 10, 11), (2018, 3, 4), (1960, 1, 7), (2000, 8, 7), (1962, 12, 9),
         (1982, 2, 18), (2012, 1, 8), (2002, 8, 24), (1990, 2, 1), (1990, 10, 7), (1995, 6, 23), (2022, 11, 5),
         (2004, 6, 9)]

for year, day, month in dates:
    italiandate = ItalianDate(year, day, month)
    print(italiandate.format(), italiandate.iso_format())