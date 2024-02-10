class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    @classmethod
    def from_diameter(cls, diametr):
        return cls(diametr / 2)


circle = Circle(5)
print(circle.radius)

circle = Circle.from_diameter(10)
print(circle.radius)
