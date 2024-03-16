class AttrDict:
    def __init__(self, data: dict = {}) -> None:
        self.data = dict(data)
        self.__dict__.update(self.data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data

    def __getitem__(self, value):
        return self.data[value]

    def __setitem__(self, key, value):
        self.data[key] = value
        if key in self.data:
            self.__dict__[key] = value


# INPUT DATA:

# TEST_1:
attrdict = AttrDict({"name": "X Æ A-12", "father": "Elon Musk"})

print(attrdict["name"])
print(attrdict.father)
print(len(attrdict))

# TEST_2:
attrdict = AttrDict({"name": "Timur", "city": "Moscow"})

attrdict["city"] = "Dubai"
attrdict["age"] = 31
print(attrdict.city)
print(attrdict.age)

# TEST_3:
attrdict = AttrDict()

attrdict["school_name"] = "BEEGEEK"
print(attrdict["school_name"])
print(attrdict.school_name)

# TEST_4:
d = AttrDict()
d.name = "Leonardo da Vinci"

try:
    print(d["name"])
except KeyError:
    print("Ключ отсутствует")

# TEST_5:
d = dict.fromkeys(range(100), None)
attrdict = AttrDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)
