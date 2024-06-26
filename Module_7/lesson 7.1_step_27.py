class Validator:
    def __init__(self, obj) -> None:
        self.obj = obj

    def is_valid(self):
        return None


class NumberValidator(Validator):
    def is_valid(self):
        return isinstance(self.obj, (int, float))


# INPUT DATA:

# TEST_1:
print(issubclass(NumberValidator, Validator))

# TEST_2:
validator1 = Validator("beegeek")
validator2 = Validator(1)
validator3 = Validator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())

# TEST_3:
validator1 = NumberValidator("beegeek")
validator2 = NumberValidator(1)
validator3 = NumberValidator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())

# TEST_4:
instances = [12, 34.1, [1, 2, 3], {4, 5, 6}, (7, 8, 9), {1: "one"}, "this is string"]

for instance in instances:
    validator = NumberValidator(instance)
    print(validator.is_valid())
