from collections import UserDict

class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self.d_alias = {}
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        if key in self.d_alias:
            return self.d_alias[key][0]
        raise KeyError

    def __setitem__(self, key, item) -> None:
        key_old = key
        if key in self.d_alias:
            lst = list(self.d_alias[key])
            lst[0] = item
            key_old = lst[1]
        for k, v in self.d_alias.items():
            if key_old == v[1]:
                res = list(self.d_alias[k])
                res[0] = item
                self.d_alias[k] = tuple(res)

        self.data[key_old] = item

    def __delitem__(self, key) -> None:
        return super().__delitem__(key)

    def alias(self, key, alias):
        self.d_alias[alias] = (self.data[key], key)


# INPUT DATA:

# TEST_1:
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias("x", "z")
multikeydict.alias("x", "t")
print(multikeydict["z"])
multikeydict["t"] += 1
print(multikeydict["x"])

multikeydict.alias("y", "z")
multikeydict["z"] += [30]
print(multikeydict["y"])

# TEST_2:
multikeydict = MultiKeyDict(x=100)

multikeydict.alias("x", "z")
del multikeydict["x"]
print(multikeydict["z"])

try:
    print(multikeydict["x"])
except KeyError:
    print("Ключ отстутствует")

# TEST_3:
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias("x", "y")
print(multikeydict["y"])

multikeydict["y"] += [30]
print(multikeydict["y"])

# TEST_4:
multikeydict = MultiKeyDict(lecture="python", lesson="object oriented programming")

multikeydict.alias("lecture", "lesson")
print(multikeydict["lesson"])

multikeydict.alias("lecture", "lesson")
print(multikeydict["lesson"])

del multikeydict["lesson"]
print(multikeydict["lesson"])

# TEST_5:
mkey = MultiKeyDict(x=1)
mkey.alias("x", "y")
mkey.alias("x", "z")
print(mkey["x"], mkey["y"], mkey["z"])
mkey["x"] += 1
print(mkey["x"], mkey["y"], mkey["z"])

# TEST_6:
mkey = MultiKeyDict(x=1)
mkey.alias("x", "y")
mkey.alias("x", "z")
print(mkey["x"], mkey["y"], mkey["z"])
mkey["y"] += 1
print(mkey["x"], mkey["y"], mkey["z"])

# TEST_7:
multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([("x", 1), ("y", 2), ("z", 3)])

print(multikeydict1["x"])
print(multikeydict1["y"])
print(multikeydict2["z"])

multikeydict1["a"] = 4
print(multikeydict1["a"])

# TEST_8:
multikeydict = MultiKeyDict(x=100)

multikeydict.alias("x", "z")
multikeydict.alias("x", "t")
del multikeydict["x"]
multikeydict["z"] += 1
print(multikeydict["z"])
print(multikeydict["t"])
