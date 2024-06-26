class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x, self.y}"


class Circle:
    def __init__(self, radius, center: Point) -> None:
        self.radius = radius
        self.center = center

    def __str__(self) -> str:
        return f"{self.center.__str__()}, r = {self.radius}"


# INPUT DATA:

# TEST_1:
point = Point(1, 1)
circle = Circle(5, point)

print(point)
print(circle)

# TEST_2:
points = [
    (59, 98),
    (72, 31),
    (9, 85),
    (3, 85),
    (55, 35),
    (54, 100),
    (68, 75),
    (24, 60),
    (6, 41),
    (48, 71),
    (20, 21),
    (38, 1),
    (100, 78),
    (48, 92),
    (34, 70),
    (92, 58),
    (33, 58),
    (73, 39),
    (79, 3),
    (58, 83),
    (75, 2),
    (50, 90),
    (30, 63),
    (27, 66),
    (10, 47),
    (1, 44),
    (15, 57),
    (49, 24),
    (67, 38),
    (12, 26),
    (98, 1),
    (93, 79),
    (4, 45),
    (12, 17),
    (31, 75),
    (62, 77),
    (71, 77),
    (28, 13),
    (87, 77),
    (67, 56),
    (83, 18),
    (93, 48),
    (41, 79),
    (90, 5),
    (13, 9),
    (73, 1),
    (76, 91),
    (30, 13),
    (57, 71),
    (27, 34),
    (88, 5),
    (62, 29),
    (43, 76),
    (44, 50),
    (33, 18),
    (90, 76),
    (20, 4),
    (50, 44),
    (62, 62),
    (95, 82),
    (35, 56),
    (61, 17),
    (44, 18),
    (3, 8),
    (38, 46),
    (83, 70),
    (4, 78),
    (18, 4),
    (79, 77),
    (28, 82),
    (96, 45),
    (19, 68),
    (29, 51),
    (70, 6),
    (41, 2),
    (2, 11),
    (58, 71),
    (52, 21),
    (32, 86),
    (58, 21),
    (20, 73),
    (7, 37),
    (92, 30),
    (71, 68),
    (82, 37),
    (10, 45),
    (91, 43),
    (28, 77),
    (74, 45),
    (43, 31),
    (90, 98),
    (9, 41),
    (15, 29),
    (40, 14),
    (76, 61),
    (40, 49),
    (39, 26),
    (59, 21),
    (43, 68),
    (10, 61),
]

radiuses = [
    75,
    63,
    20,
    70,
    26,
    47,
    44,
    100,
    80,
    54,
    7,
    86,
    49,
    43,
    14,
    23,
    49,
    17,
    82,
    99,
    96,
    78,
    17,
    99,
    65,
    34,
    17,
    47,
    70,
    34,
    52,
    94,
    13,
    51,
    50,
    66,
    35,
    63,
    64,
    6,
    34,
    88,
    64,
    72,
    36,
    65,
    25,
    67,
    9,
    59,
    59,
    70,
    3,
    15,
    15,
    4,
    63,
    69,
    54,
    1,
    11,
    66,
    3,
    81,
    81,
    35,
    11,
    74,
    78,
    43,
    18,
    31,
    16,
    60,
    49,
    34,
    80,
    28,
    91,
    99,
    63,
    32,
    46,
    31,
    66,
    15,
    41,
    16,
    73,
    8,
    44,
    93,
    7,
    40,
    84,
    67,
    84,
    55,
    14,
    96,
]


for i in range(100):
    x, y = points[i]
    point = Point(x, y)
    circle = Circle(radiuses[i], point)
    print(point)
    print(circle)
