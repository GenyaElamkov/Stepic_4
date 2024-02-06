from math import sqrt


class QuadraticPolynomial:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self) -> int | float | None:
        try:
            member = sqrt(self.b**2 - (4 * self.a * self.c))
            return (-self.b - member) / (2 * self.a)
        except ValueError:
            return None

    @property
    def x2(self) -> int | float | None:
        try:
            member = sqrt(self.b**2 - (4 * self.a * self.c))
            return (-self.b + member) / (2 * self.a)
        except ValueError:
            return None

    @property
    def view(self) -> str:
        return f"{self.a}x^2 + {self.b}x + {self.c}".replace("+ -", "- ")

    @property
    def coefficients(self) -> tuple[int | float]:
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, coef: tuple) -> None:
        self.a, self.b, self.c = coef


polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)
