import inflection


def snake_case(attrs: bool = False):
    def wrapper(cls):
        arr = [name for name in cls.__dict__ if not name.startswith("__")]
        for name in arr:
            value = getattr(cls, name)

            if not callable(value) == attrs or attrs:
                setattr(cls, inflection.underscore(name), value)
                delattr(cls, name)

        return cls

    return wrapper


# INPUT DATA:


# TEST_1:
@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1

    def superSecondMethod(self):
        return 2


obj = MyClass()

print(obj.first_method())
print(obj.super_second_method())


# TEST_2:
@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2


print(MyClass.first_attr)
print(MyClass.super_second_attr)


# TEST_3:
@snake_case()
class MyClass:
    FirstAttr = 1

    def FirstMethod(self):
        return 1


obj = MyClass()

print(MyClass.FirstAttr)
print(obj.first_method())


# TEST_4:
@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

    def __init__(self):
        self.MyName = "John Doe"


obj = MyClass()
print(obj.MyName)

myclass_attrs = ["FirstAttr", "superSecondAttr"]

for attr in myclass_attrs:
    try:
        print(MyClass.__dict__[attr])
    except KeyError:
        print("атрибут отсутствует")


# TEST_5:
@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1

    def superSecondMethod(self):
        return 2


obj = MyClass()

myclass_attrs = ["FirstMethod", "superSecondMethod"]

for method in myclass_attrs:
    try:
        print(obj.__dict__[method])
    except KeyError:
        print("метод отсутствует")


# TEST_6:
@snake_case()
class MyClass:
    def _FirstMethod(self):
        return 1

    def _superSecondMethod(self):
        return 2


obj = MyClass()

print(obj._first_method())
print(obj._super_second_method())
