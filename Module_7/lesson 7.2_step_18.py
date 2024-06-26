class Triangle:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side) -> None:
        super().__init__(side, side, side)


# INPUT DATA:

# TEST_1:
print(issubclass(EquilateralTriangle, Triangle))

# TEST_2:
triangle1 = Triangle(3, 4, 5)
triangle2 = EquilateralTriangle(3)

print(triangle1.perimeter())
print(triangle2.perimeter())

# TEST_3:
digits = [
    (124, 70, 54),
    (141, 136, 137),
    (171, 100, 170),
    (64, 175, 23),
    (101, 75, 188),
    (179, 56, 126),
    (149, 192, 22),
    (88, 120, 116),
    (102, 185, 105),
    (32, 46, 172),
    (61, 115, 180),
    (182, 108, 92),
    (124, 141, 134),
    (24, 115, 167),
    (96, 23, 150),
    (92, 92, 107),
    (29, 57, 27),
    (38, 118, 102),
    (21, 180, 96),
    (187, 142, 104),
    (71, 32, 155),
    (171, 177, 37),
    (38, 174, 107),
    (56, 147, 103),
    (50, 193, 99),
    (76, 155, 178),
    (106, 111, 142),
    (155, 83, 91),
    (35, 108, 106),
    (113, 181, 173),
    (134, 63, 37),
    (83, 93, 184),
    (152, 97, 83),
    (107, 165, 99),
    (193, 151, 160),
    (57, 188, 54),
    (145, 173, 115),
    (127, 29, 43),
    (143, 23, 173),
    (151, 194, 32),
    (112, 115, 150),
    (200, 183, 100),
    (152, 199, 116),
    (106, 176, 136),
    (94, 161, 60),
    (146, 195, 163),
    (195, 162, 97),
    (88, 57, 26),
    (151, 150, 110),
    (171, 170, 107),
]

for a, b, c in digits:
    triangle = Triangle(a, b, c)
    print(triangle.perimeter())

# TEST_4:
digits = [
    44,
    143,
    173,
    116,
    191,
    78,
    162,
    60,
    125,
    27,
    65,
    43,
    55,
    84,
    101,
    91,
    55,
    57,
    74,
    64,
    48,
    133,
    129,
    171,
    58,
    103,
    80,
    112,
    45,
    61,
    159,
    167,
    42,
    119,
    131,
    143,
    91,
    58,
    26,
    40,
    59,
    120,
    168,
    125,
    27,
    144,
    130,
    179,
    63,
    168,
]

for side in digits:
    equilateraltriangle = EquilateralTriangle(side)
    print(equilateraltriangle.perimeter())
