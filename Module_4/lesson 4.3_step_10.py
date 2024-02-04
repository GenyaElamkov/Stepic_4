from math import sqrt


class Vector:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def abs(self):
        return sqrt((self.x**2 + self.y**2))


vector = Vector()

print(vector.x, vector.y)
print(vector.abs())

vector = Vector(3, 4)

print(vector.x, vector.y)
print(vector.abs())
