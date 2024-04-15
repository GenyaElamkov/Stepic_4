class FieldTracker:
    data = {}

    def __init__(self) -> None:
        __class__.data = {k: [v] for k, v in self.__dict__.items()}

    def __setattr__(self, __name: str, __value) -> None:
        if __name in self.__dict__:
            __class__.data[__name].append(__value)
        self.__dict__[__name] = __value

    def base(self, attr):
        return __class__.data[attr][0]

    def has_changed(self, attr):
        return True if len(__class__.data[attr]) > 1 else False

    def changed(self):
        return {k: v[0] for k, v in __class__.data.items() if len(v) > 1}

    def save(self):
        __class__.data = {k: [v[-1]] for k, v in __class__.data.items()}


# class FieldTracker:
#     def __init__(self):
#         self._values = {
#             field: getattr(self, field)
#             for field in self.fields
#         }

#     def base(self, field):
#         return self._values[field]

#     def has_changed(self, field):
#         return self._values[field] != getattr(self, field)
    
#     def changed(self):
#         return {
#             field: self.base(field)
#             for field in self.fields
#             if self.has_changed(field)
#         }

#     def save(self):
#         for field in self.fields:
#             self._values[field] = getattr(self, field)


# INPUT DATA:


# TEST_1:
class Point(FieldTracker):
    fields = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)

print(point.base("x"))
print(point.has_changed("x"))
print(point.changed())


# TEST_2:
class Point(FieldTracker):
    fields = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.z = 5

print(point.base("x"))
print(point.base("z"))
print(point.has_changed("x"))
print(point.has_changed("z"))
print(point.changed())


# TEST_3:
class Point(FieldTracker):
    fields = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


point = Point(1, 2, 3)
point.x = 0
point.z = 4
point.save()

print(point.base("x"))
print(point.base("z"))
print(point.has_changed("x"))
print(point.has_changed("z"))
print(point.changed())


# TEST_4:
class Point(FieldTracker):
    fields = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.changed())
p.x = 4
print(p.changed())
print(p.x)
p.z = 6
print(p.changed())
p.save()
print(p.changed())
p.y = 8
print(p.changed())
print(p.y)
p.save()
print(p.changed())
p.save()
print(p.changed())


# TEST_5:
class Point(FieldTracker):
    fields = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.has_changed("x"))
print(p.has_changed("y"))
print(p.has_changed("z"))
p.x = 4
print(p.has_changed("x"))
print(p.has_changed("y"))
print(p.has_changed("z"))
p.z = 6
print(p.has_changed("x"))
print(p.has_changed("y"))
print(p.has_changed("z"))
p.save()
print(p.has_changed("x"))
print(p.has_changed("y"))
print(p.has_changed("z"))
p.y = 8
print(p.has_changed("x"))
print(p.has_changed("y"))
print(p.has_changed("z"))
p.save()
print(p.has_changed("x"))
print(p.has_changed("y"))
print(p.has_changed("z"))


# TEST_6:
class Point(FieldTracker):
    fields = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.base("x"))
p.x = 4
print(p.base("x"))
print(p.x)
p.z = 6
print(p.base("x"))
print(p.base("y"))
print(p.base("z"))
p.save()
print(p.base("x"))
print(p.base("y"))
print(p.base("z"))
p.y = 8
print(p.base("y"))
print(p.y)
p.save()
print(p.base("y"))
