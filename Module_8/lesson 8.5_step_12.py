import functools
import json


def jsonattr(filename):
    def wrapper(cls):
        old_init = cls.__init__
        with open(filename, "r") as file:
            for k, v in json.load(file).items():
                setattr(cls, k, v)

        @functools.wraps(old_init)
        def new_init(self, *args, **kwargs):
            old_init(self, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return wrapper


# INPUT DATA:

# TEST_1:
with open("test.json", "w") as file:
    file.write('{"x": 1, "y": 2}')


@jsonattr("test.json")
class MyClass:
    pass


print(MyClass.x)
print(MyClass.y)

# TEST_2:
with open("test.json", "w") as file:
    file.write('{"name": "John", "surname": "Doe"}')


@jsonattr("test.json")
class Person:
    pass


print(Person.name)
print(Person.surname)

# TEST_3:
with open("test.json", "w") as file:
    file.write('{"name": "Кемаль", "breed": "Британский"}')


@jsonattr("test.json")
class Cat:
    def __init__(self, name=None, breed=None):
        self.name = name or self.name
        self.surname = breed or self.breed


cat = Cat()
print(cat.name)
print(cat.breed)

# TEST_4:
with open("test.json", "w") as file:
    file.write('{"shoot1": "pif", "shoot2": "paf"}')


@jsonattr("test.json")
class Gun:
    def shoot(self):
        print(self.shoot1)
        print(self.shoot2)


gun = Gun()
gun.shoot()
