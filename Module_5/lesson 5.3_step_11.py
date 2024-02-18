class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{__class__.__name__}({self.x}, {self.y})"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, tuple) and len(__value) == 2:
            x, y = __value
            return self.x == x and self.y == y

        if isinstance(__value, __class__):
            return self.x == __value.x and self.y == __value.y
        return NotImplemented


a = Vector(1, 2)
b = Vector(1, 2)

print(a == b)
print(a != b)


a = Vector(1, 2)
pair1 = (1, 2)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)

print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
print(a == pair5)
