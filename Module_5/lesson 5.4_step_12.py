from math import sqrt


class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x, self.y}"

    def __repr__(self) -> str:
        return f"{__class__.__name__}{self.x, self.y}"

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __pos__(self):
        return __class__(self.x, self.y)

    def __neg__(self):
        return __class__(-self.x, -self.y)


vector = Vector(3, -4)

print(+vector)
print(-vector)
print(abs(vector))
