def limiter(limit: int, unique: str, lookup: str):
    instances = {}

    def wrapper(cls):
        cls.instance_count = 0

        def new_init(*args, **kwargs):
            obj = cls(*args, **kwargs)

            instance_id = getattr(obj, unique)

            if instance_id in instances:
                return instances[instance_id]

            if cls.instance_count == limit:
                if lookup == "FIRST":
                    return list(instances.values())[0]
                elif lookup == "LAST":
                    return list(instances.values())[-1]

            instances.setdefault(instance_id, obj)
            cls.instance_count += 1
            return obj

        return new_init

    return wrapper


# INPUT DATA:


# TEST_1:
@limiter(2, "ID", "FIRST")
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value


obj1 = MyClass(1, 5)  # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8)  # создается экземпляр класса с идентификатором 2

obj3 = MyClass(
    1, 20
)  # возвращается obj1, так как экземпляр с идентификатором 1 уже есть
obj4 = MyClass(
    3, 0
)  # превышено ограничение limit, возвращается первый созданный экземпляр

print(obj3.value)
print(obj4.value)


# TEST_2:
@limiter(3, "ID", "LAST")
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value


obj1 = MyClass(1, 5)  # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8)  # создается экземпляр класса с идентификатором 2
obj3 = MyClass(3, 10)  # создается экземпляр класса с идентификатором 3

obj4 = MyClass(
    4, 0
)  # превышено ограничение limit, возвращается последний созданный экземпляр
obj5 = MyClass(
    2, 20
)  # возвращается obj2, так как экземпляр с идентификатором 2 уже есть

print(obj4.value)
print(obj5.value)


# TEST_3:
@limiter(10, "uniq", "LAST")
class MyClass:
    def __init__(self, uniq, value):
        self.uniq = uniq
        self.value = value


values = [
    (0, 48),
    (1, 17),
    (2, 36),
    (3, 26),
    (4, 52),
    (5, 90),
    (6, 98),
    (7, 46),
    (8, 86),
    (9, 95),
    (10, 35),
    (11, 84),
    (12, 64),
    (13, 30),
    (14, 30),
    (15, 16),
    (16, 22),
    (17, 96),
    (18, 41),
    (19, 31),
]

for ID, value in values:
    obj = MyClass(ID, value)
    print(f"ID = {obj.uniq}, value = {obj.value}")


# TEST_4:
@limiter(10, "my_id", "FIRST")
class MyClass:
    def __init__(self, value, my_id):
        self.my_id = my_id
        self.value = value


values = [
    (84, 0),
    (97, 1),
    (41, 2),
    (80, 3),
    (31, 4),
    (40, 5),
    (26, 6),
    (51, 7),
    (68, 8),
    (41, 9),
    (76, 10),
    (56, 11),
    (96, 12),
    (48, 13),
    (87, 14),
    (86, 15),
    (88, 16),
    (52, 17),
    (13, 18),
    (82, 19),
]

for value, ID in values:
    obj = MyClass(value, ID)
    print(f"ID = {obj.my_id}, value = {obj.value}")


# TEST_5:
@limiter(12, "my_id", "LAST")
class MyClass:
    def __init__(self, value, my_id):
        self.my_id = my_id
        self.value = value


values = [
    (33, 0),
    (99, 1),
    (71, 2),
    (61, 3),
    (51, 4),
    (76, 5),
    (25, 6),
    (95, 7),
    (67, 8),
    (54, 9),
    (62, 10),
    (66, 11),
    (73, 3),
    (46, 9),
    (52, 9),
    (93, 10),
    (76, 6),
    (86, 8),
    (38, 4),
    (67, 8),
    (14, 12),
]

for value, ID in values:
    obj = MyClass(value, ID)
    print(f"ID = {obj.my_id}, value = {obj.value}")


# TEST_6:
@limiter(3, "my_id", "LAST")
class MyClass:
    def __init__(self, value, my_id):
        self.my_id = my_id
        self.value = value


obj1 = MyClass(12, 0)
obj2 = MyClass(24, 1)
obj3 = MyClass(36, 2)

obj4 = MyClass(48, 3)
obj5 = MyClass(60, 1)

print(obj4 is obj3)
print(obj5 is obj2)


# TEST_7:
@limiter(3, "my_id", "FIRST")
class MyClass:
    def __init__(self, value, my_id):
        self.my_id = my_id
        self.value = value


obj1 = MyClass(12, 0)
obj2 = MyClass(24, 1)
obj3 = MyClass(36, 2)

obj4 = MyClass(48, 3)
print(obj4 is obj1)
