class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Вектор на плоскости с координатами ({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"