class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates) -> None:
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self) -> str:
        return f"{__class__.__name__}{self.proteins, self.fats, self.carbohydrates}"

    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(
                self.proteins + other.proteins,
                self.fats + other.fats,
                self.carbohydrates + other.carbohydrates,
            )
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return __class__(self.proteins * n, self.fats * n, self.carbohydrates * n)
        return NotImplemented

    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return __class__(self.proteins / n, self.fats / n, self.carbohydrates / n)
        return NotImplemented

    def __floordiv__(self, n):
        if isinstance(n, (int, float)):
            return __class__(
                self.proteins // n, self.fats // n, self.carbohydrates // n
            )
        return NotImplemented


food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 10, 20)

print(food1 + food2)
print(food1 * 2)
print(food1 / 2)
print(food1 // 2)
