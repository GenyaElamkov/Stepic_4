from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(default=0, compare=False)

    def __post_init__(self):
        if self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2

    def symmetric_x(self):
        return __class__(self.x, -1 * self.y)

    def symmetric_y(self):
        return __class__(-1 * self.x, self.y)


    # def __post_init__(self):
    #     if self.x > 0 and self.y != 0:
    #         self.quadrant = (1, 4)[self.y < 0]
    #     elif self.x < 0 and self.y != 0:
    #         self.quadrant = (2, 3)[self.y < 0]

    # def symmetric_x(self):
    #     return type(self)(self.x, -self.y)

    # def symmetric_y(self):
    #     return type(self)(-self.x, self.y)


# INPUT DATA:

# TEST_1:
point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)

# TEST_2:
point = Point(1.0, 2.0)

print(point.symmetric_x())
print(point.symmetric_y())

# # TEST_3:
# point1 = Point(1, 2)
# point2 = Point(1, 2)
# point3 = Point(3, 4)

# print(point1 == point2)
# print(point1 == point3)
# print(point2 != point3)

# # TEST_4:
# for x in range(-3, 4):
#     for y in range(-3, 4):
#         point = Point(x, y)
#         print(point)

# # TEST_5:
# for x in range(-3, 4):
#     for y in range(-3, 4):
#         point = Point(x, y)
#         print(point.symmetric_x())

# # TEST_6:
# for x in range(-3, 4):
#     for y in range(-3, 4):
#         point = Point(x, y)
#         print(point.symmetric_y())
