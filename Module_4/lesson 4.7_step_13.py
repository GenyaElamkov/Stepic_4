class QuadraticPolynomial:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)

    @classmethod
    def from_str(cls, string) -> float:
        return cls(*map(float, string.split()))


# polynom = QuadraticPolynomial(1, -5, 6)

# print(polynom.a)
# print(polynom.b)
# print(polynom.c)

# polynom = QuadraticPolynomial.from_iterable([2, 13, -1])

# print(polynom.a)
# print(polynom.b)
# print(polynom.c)

polynom = QuadraticPolynomial.from_str("-1.5 4 14.8")

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
