class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{__class__.__name__}{self.x, self.y}"

    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, __class__):
            return __class__(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return __class__(self.x * n, self.y * n)
        return NotImplemented

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return __class__(self.x / n, self.y / n)
        return NotImplemented

    def __rmul__(self, n):
        if isinstance(n, (int, float)):
            return self.__mul__(n)
        return NotImplemented

    def __rtruediv__(self, n):
        if isinstance(n, (int, float)):
            self.__truediv__(n)
        return NotImplemented


a = Vector(3, 4)

print(a * 2)
print(2 * a)
print(a / 2)
