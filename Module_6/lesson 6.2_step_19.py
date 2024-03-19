class Grouper:
    def __init__(self, iterable, key) -> None:
        self.key = key
        self._make_group(iterable)

    def _make_group(self, iterable):
        self._dict = {}
        for elem in iterable:
            self.add(elem)

    def add(self, value) -> None:
        self._dict.setdefault(self.key(value), []).append(value)

    def group_for(self, value):
        return self.key(value)

    def __len__(self) -> int:
        return len(self._dict)

    def __iter__(self):
        yield from self._dict.items()

    def __contains__(self, item) -> bool:
        return item in self._dict

    def __getitem__(self, key):
        return self._dict[key]


# INPUT DATA:

# TEST_1:
grouper = Grouper(["bee", "geek", "one", "two", "five", "hi"], key=len)

print(grouper[2])
print(grouper[3])
print(grouper[4])

# TEST_2:
grouper = Grouper(["bee", "geek", "one", "two", "five", "hi"], key=len)

print(3 in grouper)
print("bee" in grouper)

# TEST_3:
grouper = Grouper(["hi"], key=lambda s: s[0])
print(len(grouper))

grouper.add("hello")
grouper.add("bee")
grouper.add("big")

print(len(grouper))

grouper.add("geek")
print(grouper["h"])
print(grouper["b"])
print(grouper["g"])

print(len(grouper))

# TEST_4:
grouper = Grouper(["hi"], key=lambda s: s[0])

print(grouper.group_for("hello"))
print(grouper.group_for("bee"))
print(grouper["h"])
print("b" in grouper)

# TEST_5:
data = [
    504,
    506,
    503,
    507,
    507,
    508,
    504,
    510,
    500,
    503,
    501,
    502,
    503,
    502,
    502,
    510,
    502,
    500,
    503,
    508,
    508,
    502,
    507,
    500,
    502,
    501,
    502,
    504,
    505,
    505,
    500,
    501,
    507,
    504,
    509,
    507,
    508,
    508,
    502,
    510,
    503,
    501,
    505,
    501,
    510,
    505,
    500,
    507,
    510,
    507,
    506,
    507,
    501,
    502,
    504,
    506,
    501,
    501,
    506,
    502,
    508,
    505,
    509,
    509,
    502,
    506,
    507,
    505,
    505,
    507,
    503,
    505,
    504,
    510,
    505,
    503,
    508,
    508,
    504,
    504,
    510,
    501,
    506,
    503,
    502,
    508,
    507,
    503,
    501,
    506,
    505,
    506,
    504,
    504,
    505,
    503,
    507,
    504,
    507,
    510,
]

grouper = Grouper(data, key=lambda x: x % 2 == 0)
print(grouper[True])
print(grouper[False])

# TEST_6:
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "height"])

persons = [
    Person("Tim", 63, 193),
    Person("Eva", 47, 158),
    Person("Mark", 71, 172),
    Person("Alex", 45, 193),
    Person("Jeff", 63, 193),
    Person("Ryan", 41, 184),
    Person("Ariana", 28, 158),
    Person("Liam", 69, 193),
]


grouper = Grouper(persons, key=lambda x: x.height)
print(sorted(grouper))

# TEST_7:
grouper = Grouper([], key=lambda x: x)
print(*grouper)

# TEST_8:
d = list(range(1, 100))
grouper = Grouper(d, bool)
print(*grouper)

d.append(100)
print(*grouper)

# TEST_9:
d = range(1, 100)
grouper = Grouper(d, bool)
print(*grouper)

grouper.add(100)
print(*grouper)
