class MaxCallsException(Exception): ...


class LimitedTakes:
    def __init__(self, times) -> None:
        self._times = times
        self._cnt = 0

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        
        if self._times not in obj.__dict__:
            raise AttributeError("Атрибут не найден")
        
        if self._times == self._cnt:
            raise MaxCallsException("Превышено количество доступных обращений")
        self._cnt += 1
        
        return obj.__dict__[self._times]

    def __set__(self, obj, value):
        obj.__dict__[self._times] = value


# INPUT DATA:


# TEST_1:
class Student:
    name = LimitedTakes(3)


student = Student()
student.name = "Gwen"

print(student.name)
print(student.name)
print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)


# TEST_2:
class Student:
    name = LimitedTakes(3)


student = Student()

for _ in range(100):
    student.name = "Gwen"

print(student.name)


# TEST_3:
class Programmer:
    name = LimitedTakes(1)


programmer = Programmer()

try:
    print(programmer.name)
except AttributeError as e:
    print(e)


# TEST_4:
class Programmer:
    name = LimitedTakes(1000)


programmer = Programmer()
programmer.name = "Gvido"

for _ in range(1000):
    programmer.name

try:
    print(programmer.name)
except MaxCallsException as e:
    print(e)


# TEST_5:
class Student:
    name = LimitedTakes(3)


class Programmer:
    name = LimitedTakes(1)


student = Student()
programmer = Programmer()

student.name = "Gwen"
programmer.name = "Mantrida"

for _ in range(3):
    print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)


print(programmer.name)

try:
    print(programmer.name)
except MaxCallsException as e:
    print(e)


# TEST_6:
class Student:
    first_name = LimitedTakes(3)
    last_name = LimitedTakes(1)


student = Student()

student.first_name = "Gwen"
student.last_name = "Stacy"


for _ in range(3):
    print(student.first_name)

try:
    print(student.first_name)
except MaxCallsException as e:
    print(e)

print(student.last_name)
try:
    print(student.last_name)
except MaxCallsException as e:
    print(e)


# TEST_7:
class Student:
    name = LimitedTakes(3)


print(Student.name.__class__)


# TEST_8:
class Student:
    name = LimitedTakes(3)


student = Student()
student.name = "Gwen"

print(student.name)
print(student.name)
student.name = "Mary"
print(student.name)
