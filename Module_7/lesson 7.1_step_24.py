class Shape: ...


class Circle(Shape): ...


class Polygon(Shape): ...


class Triangle(Polygon): ...


class IsoscelesTriangle(Triangle): ...


class EquilateralTriangle(Triangle): ...


class Quadrilateral(Polygon): ...


class Parallelogram(Quadrilateral): ...


class Rectangle(Parallelogram): ...


class Square(Rectangle): ...


# INPUT DATA:

# TEST_1:
print(issubclass(Circle, Shape))
print(issubclass(Polygon, Shape))

# TEST_2:
print(issubclass(Triangle, Polygon))
print(issubclass(IsoscelesTriangle, Triangle))
print(issubclass(EquilateralTriangle, Triangle))

# TEST_3:
print(issubclass(Parallelogram, Quadrilateral))
print(issubclass(Rectangle, Quadrilateral))
print(issubclass(Square, Quadrilateral))

# TEST_4:
print(issubclass(IsoscelesTriangle, Quadrilateral))
print(issubclass(EquilateralTriangle, Quadrilateral))

print(issubclass(Parallelogram, Triangle))
print(issubclass(Rectangle, Triangle))
print(issubclass(Square, Triangle))

# TEST_5:
print(issubclass(IsoscelesTriangle, Circle))
print(issubclass(EquilateralTriangle, Circle))

print(issubclass(Parallelogram, Circle))
print(issubclass(Rectangle, Circle))
print(issubclass(Square, Circle))

# TEST_6:
print(issubclass(Square, Shape))
print(issubclass(IsoscelesTriangle, Shape))
print(issubclass(EquilateralTriangle, Shape))
print(issubclass(Circle, Shape))
