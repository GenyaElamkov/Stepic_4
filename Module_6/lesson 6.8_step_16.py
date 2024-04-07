class NonNegativeInteger:
    def __init__(self, name, default=None) -> None:
        self._name = name
        self._default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._name not in obj.__dict__:
            if self._default is None:
                raise AttributeError("Атрибут не найден")
            return self._default
        return obj.__dict__[self._name]

    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Некорректное значение")
        obj.__dict__[self._name] = value

# class NonNegativeInteger:
#     def __init__(self, name, default=None):
#         self._attr = name
#         self._default = default

#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._attr not in obj.__dict__ and self._default is None:
#             raise AttributeError('Атрибут не найден')
#         return obj.__dict__.get(self._attr, self._default)

#     def __set__(self, obj, value):
#         if not isinstance(value, int) or value < 0:
#             raise ValueError('Некорректное значение')
#         obj.__dict__[self._attr] = value


# INPUT DATA:


# TEST_1:
class Student:
    score = NonNegativeInteger("score")


student = Student()
student.score = 90

print(student.score)


# TEST_2:
class Student:
    score = NonNegativeInteger("score", 0)


student = Student()

print(student.score)
student.score = 0
print(student.score)


# TEST_3:
class Student:
    score = NonNegativeInteger("score")


student = Student()

try:
    print(student.score)
except AttributeError as e:
    print(e)


# TEST_4:
class Student:
    score = NonNegativeInteger("score")


student = Student()

try:
    student.score = -90
except ValueError as e:
    print(e)


# TEST_5:
class Student:
    score = NonNegativeInteger("score")


student = Student()
student.score = 90

try:
    student.score = -90
except ValueError as e:
    print(e)


# TEST_6:
class Student:
    score = NonNegativeInteger("score")


student = Student()

not_supported = [1.2, {1: "one"}, {1, 2, 3}, [4, 5, 6], (7, 8, 9), "14"]

for item in not_supported:
    try:
        student.score = item
    except ValueError as e:
        print(e)


# TEST_7:
class Student:
    score = NonNegativeInteger("score")


print(Student.score.__class__)
