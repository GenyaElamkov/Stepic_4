class RaiseTo:
    def __init__(self, degree: int) -> None:
        self.degree = degree

    def __call__(self, x):
        return x**self.degree


raise_to_two = RaiseTo(2)

print(raise_to_two(2))
print(raise_to_two(3))
print(raise_to_two(4))
