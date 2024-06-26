from math import sqrt


class Vector:
    def __init__(self, *args) -> None:
        self.args = args

    def __str__(self) -> str:
        return f"{self.args}"

    def _value_error(self, other):
        if len(self.args) != len(other.args):
            raise ValueError("Векторы должны иметь равную длину")

    def __add__(self, other):
        self._value_error(other)
        if isinstance(other, __class__):
            return __class__(*map(lambda x, y: x + y, self.args, other.args))
        return NotImplemented

    def __sub__(self, other):
        self._value_error(other)
        if isinstance(other, __class__):
            return __class__(*map(lambda x, y: x - y, self.args, other.args))
        return NotImplemented

    def __mul__(self, other):
        self._value_error(other)
        if isinstance(other, __class__):
            return sum(map(lambda x, y: x * y, self.args, other.args))
        return NotImplemented

    def norm(self):
        return sqrt(sum(map(lambda x: x**2, self.args)))

    def __eq__(self, other: object) -> bool:
        self._value_error(other)
        if isinstance(other, __class__):
            return self.args == other.args
        return NotImplemented
    
    def __lt__(self, other):
        self._value_error(other)
        if isinstance(other, __class__):
            return self.args < other.args
        return NotImplemented

# INPUT DATA:

# TEST_1:
vector1 = Vector(1, 2, 3)
vector2 = Vector(3, 4, 5)
vector3 = Vector(5, 6, 7, 8)

print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * vector2)
print(vector3.norm())

# TEST_2:
vector1 = Vector(1, 2, 3)
vector2 = Vector(3, 4, 5)
vector3 = Vector(5, 6, 7, 8)

print(vector1 == Vector(1, 2, 3))
print(vector1 == Vector(4, 5, 6))
print(vector1 != vector2)

# TEST_3:
vector1 = Vector(1, 2, 3)
vector2 = Vector(5, 6, 7, 8)

try:
    print(vector1 == vector2)
except ValueError as e:
    print(e)

# TEST_4:
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)

vector3 = vector1 + vector2
vector4 = vector1 - vector2

print(type(vector3))
print(type(vector4))

# TEST_5:
vector = Vector(18, 21, 14, 88)
print(vector.norm())

# TEST_6:
vector1 = Vector(1, 2)
vector2 = Vector(3, 4, 5)

operations = [
    "vector1 + vector2",
    "vector1 - vector2",
    "vector1 * vector2",
    "vector1 != vector2",
]

for operation in operations:
    try:
        eval(operation)
    except ValueError as e:
        print(e)

# TEST_7:
coordinates = [
    (14, 51, 47),
    (39, 17, 64),
    (43, 20, 88),
    (42, 12, 66),
    (74, 81, 82),
    (27, 12, 48),
    (26, 73, 15),
    (88, 46, 70),
    (45, 35, 20),
    (31, 100, 51),
    (36, 71, 28),
    (33, 51, 46),
    (60, 62, 76),
    (74, 92, 58),
    (83, 74, 29),
    (96, 47, 60),
    (63, 62, 77),
    (76, 65, 46),
    (64, 33, 67),
    (79, 95, 30),
]

for x, y, z in coordinates:
    vector = Vector(x, y, z)
    print(vector + vector, vector - vector, vector * vector, vector.norm())

# TEST_8:
coordinates = [
    ((64, 42, 11), (20, 40, 64)),
    ((50, 96, 60), (32, 26, 38)),
    ((46, 95, 64), (23, 70, 78)),
    ((22, 29, 48), (21, 50, 31)),
    ((40, 50, 19), (95, 37, 78)),
    ((74, 21, 77), (74, 21, 77)),
    ((55, 33, 88), (55, 33, 88)),
    ((99, 50, 74), (77, 28, 87)),
    ((64, 65, 33), (24, 73, 76)),
    ((63, 12, 36), (80, 53, 22)),
    ((92, 15, 80), (48, 42, 17)),
    ((84, 65, 80), (72, 15, 46)),
    ((54, 48, 52), (68, 25, 26)),
    ((37, 93, 12), (16, 76, 42)),
    ((45, 91, 87), (46, 91, 58)),
    ((33, 74, 85), (13, 20, 36)),
    ((63, 12, 43), (63, 12, 43)),
    ((87, 67, 41), (41, 82, 52)),
    ((10, 63, 68), (54, 36, 65)),
    ((74, 51, 90), (30, 25, 90)),
]

for coord1, coord2 in coordinates:
    vector1 = Vector(*coord1)
    vector2 = Vector(*coord2)
    print(vector1 == vector2, vector1 != vector2)
