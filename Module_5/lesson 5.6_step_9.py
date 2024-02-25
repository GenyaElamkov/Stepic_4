from operator import add, sub, mul, truediv


class Calculator:
    def __call__(self, a, b, operation):
        try:
            oper = {
                "+": add,
                "-": sub,
                "*": mul,
                "/": truediv,
            }
            return oper[operation](a, b)
        except ZeroDivisionError:
            return 'Деление на ноль невозможно'
        
calculator = Calculator()

print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))

calculator = Calculator()

try:
    print(calculator(10, 0, '/'))
except ValueError as e:
    print(e)