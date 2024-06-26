class AdvancedList(list):
    def join(self, _value=" "):
        return _value.join(map(str, self))

    def map(self, func):
        self[:] = map(func, self)
        # return self

    def filter(self, func):
        self[:] = filter(func, self)
        # return self


# INPUT DATA:

# TEST_1:
advancedlist = AdvancedList([1, 2, 3, 4, 5])

print(advancedlist.join())
print(advancedlist.join("-"))

# TEST_2:
advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.map(lambda x: -x)

print(advancedlist)

# TEST_3:
advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.filter(lambda x: x % 2 == 0)

print(advancedlist)

# TEST_4:
advancedlist = AdvancedList([0, 1, 2, "", 3, (), 4, 5, False, {}])
id1 = id(advancedlist)

advancedlist.filter(bool)
id2 = id(advancedlist)

print(advancedlist)
print(id1 == id2)

# TEST_5:
advancedlist = AdvancedList([1, 2, 3, 4, 5])
separators = [" - ", " + ", " = ", " * ", " / ", " ! ", " 0 ", " & ", " ^ ", " -> "]

for separator in separators:
    print(advancedlist.join(separator))

# TEST_6:
advancedlist = AdvancedList(["hello", "Gvido", "how", "are", "you"])
advancedlist.map(len)
print(advancedlist)
