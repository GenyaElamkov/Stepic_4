from math import sqrt


class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def calculates_module(self):
        return sqrt(self.x**2 + self.y**2)

    def __str__(self) -> str:
        return f"{self.x, self.y}"

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __int__(self):
        return int(self.calculates_module())

    def __float__(self):
        return float(self.calculates_module())

    def __complex__(self):
        return complex(self.x, self.y)


vector = Vector(3, 4)

print(vector)
print(int(vector))
print(float(vector))
print(complex(vector))
