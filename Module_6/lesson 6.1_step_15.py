class Point:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    @property
    def _fields(self):
        return self.x, self.y, self.z

    def __repr__(self) -> str:
        return f"{__class__.__name__}{self._fields}"

    def __iter__(self):
        yield from self._fields

    # def __next__(self):
    #     return self._fields


point = Point(1, 2, 3)

print(list(point))
# print(point)

point = Point(1, 2, 3)
x, y, z = point

print(x, y, z)

points = [Point(4, 7, 0), Point(1, 5, 10), Point(12, 23, 44)]
print(points)
