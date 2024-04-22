def auto_repr(args, kwargs):
    def wrapper(cls):
        old_repr = cls.__repr__

        def new_repr(self):
            old_repr(self)
            res_args = [repr(getattr(self, k)) for k in args]
            res_kwargs = [f"{k}={getattr(self, k)!r}" for k in kwargs]
            res = res_args + res_kwargs
            return f"{cls.__name__}({', '.join(map(str, res))})"

        cls.__repr__ = new_repr
        return cls

    return wrapper


# def auto_repr(args, kwargs):
#     def wrapper(cls):
#         def __repr__(self):
#             cls_args = [repr(self.__dict__[k]) for k in args]
#             cls_kwargs = [f'{k}={self.__dict__[k]!r}' for k in kwargs]
#             return f'{type(self).__name__}({", ".join(cls_args + cls_kwargs)})'

#         cls.__repr__ = __repr__
#         return cls

#     return wrapper

# INPUT DATA:


# TEST_1:
@auto_repr(args=["x", "y"], kwargs=["color"])
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


point = Point(1, 2, color="green")
print(point)

point.x = 10
point.y = 20
print(point)


# TEST_2:
@auto_repr(args=["name", "surname"], kwargs=[])
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


person = Person("Gvido", "van Rossum")

print(person)


# TEST_3:
@auto_repr(args=[], kwargs=["name", "breed"])
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


cat = Cat("Кемаль", "Британский")

print(cat)


# TEST_4:
@auto_repr(args=[], kwargs=[])
class Gun:
    pass


gun = Gun()

print(gun)
