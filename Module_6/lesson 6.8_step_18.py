class TypeChecked:
    def __init__(self, *name) -> None:
        self._name = name

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self 
        if self._attr not in obj.__dict__:
            raise AttributeError("Атрибут не найден")
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        if not type(value) in self._name:
            raise TypeError("Некорректное значение")
        obj.__dict__[self._attr] = value


# INPUT DATA:

# TEST_1:
class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

print(student.name)

# TEST_2:
class Student:
    name = TypeChecked(str)

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

# TEST_3:
class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

try:
    student.name = 99
except TypeError as e:
    print(e)

print(student.name)

# TEST_4:
class Student:
    age = TypeChecked(int, float)

student = Student()

student.age = 18
print(student.age)

student.age = 18.5
print(student.age)

# TEST_5:
class Vector:
    x = TypeChecked(float)
    y = TypeChecked(float)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} {self.y}'

pairs = [('12', '89'), ([1, 2], [3, 4]), ({1: 2}, {3: 4}), (True, False), (1.2, 3.4)]

for x, y in pairs:
    try:
        vector = Vector(x, y)
        print(vector)
    except TypeError as e:
        print(e)

# TEST_6:
class Student:
    name = TypeChecked(str)

print(Student.name.__class__)