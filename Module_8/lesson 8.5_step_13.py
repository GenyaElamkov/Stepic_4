import functools


def singleton(cls):
    old_new = cls.__new__
    cls._instance = None

    @functools.wraps(old_new)
    def new_new(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = old_new(cls)
        return cls._instance

    cls.__new__ = new_new
    return cls


# INPUT DATA:


# TEST_1:
@singleton
class MyClass:
    pass


obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)


# TEST_2:
@singleton
class MyClass:
    pass


instances = [MyClass() for _ in range(100)]
obj = MyClass()
print(all(instance is obj for instance in instances))


# TEST_3:
@singleton
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name!r})"


instances = [Person("John Doe") for _ in range(1000)]
person = Person("Doe John")
print(person)
print(instances[389])
print(all(instance is person for instance in instances))
