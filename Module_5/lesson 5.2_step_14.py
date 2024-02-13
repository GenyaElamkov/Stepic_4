class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self) -> str:
        return f"Rectangle({self.length}, {self.width})"


