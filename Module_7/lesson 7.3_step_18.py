class RoundedInt(int):
    def __new__(cls, num: int, even: bool = True):
        if num % 2 == 1 and even:
            num += 1
        if num % 2 == 0 and not even:
            num += 1

        return super().__new__(cls, num)


# INPUT DATA:

# TEST_1:
print(RoundedInt(7))
print(RoundedInt(8))
print(RoundedInt(7, False))
print(RoundedInt(8, False))

# TEST_2:
roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))

# TEST_3:
print(issubclass(RoundedInt, int))

# TEST_4:
for digit in range(100):
    print(RoundedInt(digit))

# TEST_5:
for digit in range(100):
    print(RoundedInt(digit, False))
