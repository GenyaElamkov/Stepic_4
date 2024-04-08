class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr
        self._history = {}

    def __get__(self, obj, cls):
        if obj is None:
            return self

        if self._attr not in obj.__dict__:
            raise AttributeError("Атрибут не найден")
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        self._history.setdefault(obj, []).append(value)
        obj.__dict__[self._attr] = value

    def get_version(self, obj, n):
        return self._history[obj][n - 1]

    def set_version(self, obj, n):
        obj.__dict__[self._attr] = self._history[obj][n - 1]


# class Versioned:
#     def __init__(self):
#         self._history = {}

#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if obj not in self._history:
#             raise AttributeError('Атрибут не найден')
#         version = self._history[obj][0]
#         values = self._history[obj][1]
#         return values[version]

#     def __set__(self, obj, value):
#         values = self._history.setdefault(obj, [-1, []])[1]
#         values.append(value)

#     def get_version(self, obj, n):
#         values = self._history[obj][1]
#         return values[n - 1]

#     def set_version(self, obj, n):
#         self._history[obj][0] = n - 1

# INPUT DATA:


# TEST_1:
class Student:
    age = Versioned()


student = Student()


# TEST_2:
class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
print(Student.age.get_version(student, 1))
print(Student.age.get_version(student, 2))
print(Student.age.get_version(student, 3))


# TEST_3:
class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)
Student.age.set_version(student, 1)
print(student.age)


# TEST_4:
class Student:
    name = Versioned()


student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)


# TEST_5:
class Person:
    age = Versioned()


person = Person()

person.age = 0
for _ in range(50):
    person.age += 1

for i in range(51):
    print(Person.age.get_version(person, i + 1))


# TEST_6:
class Person:
    age = Versioned()


person = Person()

person.age = 0
for _ in range(50):
    person.age += 1

print(person.age)
Person.age.set_version(person, 32)
print(person.age)


# TEST_7:
class Student:
    age = Versioned()


student1 = Student()
student2 = Student()

student1.age = 18
student1.age = 19
student1.age = 20

student2.age = 30
student2.age = 31
student2.age = 32

print(student1.age)
print(student2.age)
Student.age.set_version(student1, 1)
Student.age.set_version(student2, 2)
print(student1.age)
print(student2.age)


# TEST_8:
class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19
student.age = 20

print(student.age)

Student.age.set_version(student, 1)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))

Student.age.set_version(student, 2)

print(student.age)
for i in range(3):
    print(Student.age.get_version(student, i + 1))


# TEST_9:
class Student:
    age = Versioned()


print(Student.age.__class__)
student.age = 18
student.age = 19

print(student.age)
