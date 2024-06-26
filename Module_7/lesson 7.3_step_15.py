class FuzzyString(str):
    def __new__(cls, obj):
        return super().__new__(cls, str(obj).lower())

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, str):
            return NotImplemented
        return super().__eq__(__value.lower())

    def __ne__(self, __value: object) -> bool:
        if not isinstance(__value, str):
            return NotImplemented
        return super().__ne__(__value.lower())

    def __lt__(self, __value: str) -> bool:
        if not isinstance(__value, str):
            return NotImplemented
        return super().__lt__(__value.lower())

    def __gt__(self, __value: str) -> bool:
        if not isinstance(__value, str):
            return NotImplemented
        return super().__gt__(__value.lower())

    def __le__(self, __value: str) -> bool:
        if not isinstance(__value, str):
            return NotImplemented
        return super().__le__(__value.lower())

    def __ge__(self, __value: str) -> bool:
        if not isinstance(__value, str):
            return NotImplemented
        return super().__ge__(__value.lower())

    def __contains__(self, __key: str) -> bool:
        return super().__contains__(__key)


# INPUT DATA:

# TEST_1:
s1 = FuzzyString("BeeGeek")
s2 = FuzzyString("beegeek")

print(s1 == s2)
print(s1 in s2)
print(s2 in s1)
print(s2 not in s1)

# TEST_2:
s = FuzzyString("BeeGeek")

print(s != "BEEGEEK")
print(s == "BEEGEEK")
print(s != "beegeek")
print(s == "beegeek")
print(s >= "BEEGEEK")
print(s <= "BEEGEEK")
print(s > "BEEGEEK")
print(s < "BEEGEEK")

# TEST_3:
s = FuzzyString("BeeGeek")

print(s != "BEE GEEK")
print(s == "BEE GEEK")
print(s != "bee geek")
print(s == "bee geek")

# TEST_4:
s = FuzzyString("patrick")

words = [
    "patrick",
    "Patrick",
    "pAtrick",
    "PAtrick",
    "paTrick",
    "PaTrick",
    "pATrick",
    "PATrick",
    "patRick",
    "PatRick",
    "pAtRick",
    "PAtRick",
    "paTRick",
    "PaTRick",
    "pATRick",
    "PATRick",
    "patrIck",
    "PatrIck",
    "pAtrIck",
    "PAtrIck",
    "paTrIck",
    "PaTrIck",
    "pATrIck",
    "PATrIck",
    "patRIck",
    "PatRIck",
    "pAtRIck",
    "PAtRIck",
    "paTRIck",
    "PaTRIck",
    "pATRIck",
    "PATRIck",
    "patriCk",
    "PatriCk",
    "pAtriCk",
    "PAtriCk",
    "paTriCk",
    "PaTriCk",
    "pATriCk",
    "PATriCk",
    "patRiCk",
    "PatRiCk",
    "pAtRiCk",
    "PAtRiCk",
    "paTRiCk",
    "PaTRiCk",
    "pATRiCk",
    "PATRiCk",
    "patrICk",
    "PatrICk",
    "pAtrICk",
    "PAtrICk",
    "paTrICk",
    "PaTrICk",
    "pATrICk",
    "PATrICk",
    "patRICk",
    "PatRICk",
    "pAtRICk",
    "PAtRICk",
    "paTRICk",
    "PaTRICk",
    "pATRICk",
    "PATRICk",
    "patricK",
    "PatricK",
    "pAtricK",
    "PAtricK",
    "paTricK",
    "PaTricK",
    "pATricK",
    "PATricK",
    "patRicK",
    "PatRicK",
    "pAtRicK",
    "PAtRicK",
    "paTRicK",
    "PaTRicK",
    "pATRicK",
    "PATRicK",
    "patrIcK",
    "PatrIcK",
    "pAtrIcK",
    "PAtrIcK",
    "paTrIcK",
    "PaTrIcK",
    "pATrIcK",
    "PATrIcK",
    "patRIcK",
    "PatRIcK",
    "pAtRIcK",
    "PAtRIcK",
    "paTRIcK",
    "PaTRIcK",
    "pATRIcK",
    "PATRIcK",
    "patriCK",
    "PatriCK",
    "pAtriCK",
    "PAtriCK",
    "paTriCK",
    "PaTriCK",
    "pATriCK",
    "PATriCK",
    "patRiCK",
    "PatRiCK",
    "pAtRiCK",
    "PAtRiCK",
    "paTRiCK",
    "PaTRiCK",
    "pATRiCK",
    "PATRiCK",
    "patrICK",
    "PatrICK",
    "pAtrICK",
    "PAtrICK",
    "paTrICK",
    "PaTrICK",
    "pATrICK",
    "PATrICK",
    "patRICK",
    "PatRICK",
    "pAtRICK",
    "PAtRICK",
    "paTRICK",
    "PaTRICK",
    "pATRICK",
    "PATRICK",
]

print(all(s == item for item in words))


# TEST_5:
s1 = FuzzyString("ManTrida")
s2 = FuzzyString("MANTRIDA")

print(s1 == s2)
print(s1 != s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1 > s2)
print(s1 < s2)

# TEST_6:
s = FuzzyString("BeeGeek")

print(s.__eq__(1))
print(s.__ne__(1.1))
print(s.__gt__(range(5)))
print(s.__lt__([1, 2, 3]))
print(s.__ge__({4, 5, 6}))
print(s.__le__({1: "one"}))

# TEST_7:
s1 = FuzzyString("BeeGeek")
s2 = FuzzyString("bee")

print(s2 in s1)
print(s1 in s2)
