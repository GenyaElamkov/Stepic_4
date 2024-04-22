import functools


def add_attr_to_class(**kws):
    def decorator(cls):
        old_init = cls.__init__
        [setattr(cls, k, v) for k, v in kws.items()]

        @functools.wraps(old_init)
        def new__init(self, *args, **kwargs):
            old_init(self, *args, **kwargs)

        cls.__init__ = new__init
        return cls

    return decorator


# INPUT DATA:


# TEST_1:
@add_attr_to_class(first_attr=1, second_attr=2)
class MyClass:
    pass


print(MyClass.first_attr)
print(MyClass.second_attr)


# TEST_2:
@add_attr_to_class(name="Кемаль", breed="Британский")
class Cat:
    pass


print(Cat.name)
print(Cat.breed)

# TEST_3:
data = {"name": "John", "surname": "Doe"}


@add_attr_to_class(**data)
class Person:
    def __init__(self, name=None, surname=None):
        self.name = name or self.name
        self.surname = surname or self.surname


person = Person()
print(person.name)
print(person.surname)


# TEST_4:
@add_attr_to_class(shoot1="pif", shoot2="paf")
class Gun:
    def shoot(self):
        print(self.shoot1)
        print(self.shoot2)


gun = Gun()
gun.shoot()
