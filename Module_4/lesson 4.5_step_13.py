class Rectangle:
    def __init__(self, length: int | float, width: int | float) -> None:
        self.length = length
        self.width = width

    def get_perimeter(self) -> int | float:
        return self.length * 2 + self.width * 2

    def get_area(self) -> int | float:
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)


rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
