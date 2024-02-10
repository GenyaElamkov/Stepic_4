class Rectangle:
    def __init__(self, length, width) -> None:
        self._length = length
        self._width = width

    @classmethod
    def square(cls, side) -> classmethod:
        return cls(length=side, width=side)

    @property
    def length(self) -> int | float:
        return self._length

    @property
    def width(self) -> int | float:
        return self._width


rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)

rectangle = Rectangle.square(5)

print(rectangle.length)
print(rectangle.width)
