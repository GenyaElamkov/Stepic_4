from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, item) -> None:
        super().__setitem__(key, item)
        self.data[item] = key


# class TwoWayDict(UserDict):
#     def __setitem__(self, key, value):
#         self.data[key] = value
#         self.data[value] = key


# INPUT DATA:

# TEST_1:
twowaydict = TwoWayDict({'apple': 1})

twowaydict['banana'] = 2

print(twowaydict['apple'])
print(twowaydict[1])
print(twowaydict['banana'])
print(twowaydict[2])

# TEST_2:
d = TwoWayDict()
d[3] = 8
d[7] = 6
print(d[3], d[8])
print(d[7], d[6])

d.update({9: 7, 8: 2})
print(d[9], d[7])
print(d[8], d[2])

# TEST_3:
d = TwoWayDict()

for i in range(100):
    d[i] = i + 100

print(d)

# TEST_4:
from string import ascii_uppercase, ascii_lowercase

d = TwoWayDict()

for i in range(26):
    d[ascii_uppercase[i]] = ascii_lowercase[i]

print(d)