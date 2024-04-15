class SuperInt(int):
    def repeat(self, n: int = 2):
        tmp = str(abs(self)) * n
        tmp = "-" + tmp if self < 0 else tmp
        return __class__(tmp)

    def to_bin(self):
        return f"{self:b}"

    def next(self):
        return __class__(self + 1)

    def prev(self):
        return __class__(self - 1)

    def __iter__(self):
        return map(__class__, str(abs(self)))


# INPUT DATA:

# TEST_1:
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))

# TEST_2:
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.to_bin())
print(superint2.to_bin())

# TEST_3:
superint = SuperInt(17)

print(superint.prev())
print(superint.next())

# TEST_4:
superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)

# TEST_5:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
superint = SuperInt(30)

for n in digits:
    print(superint.repeat(n))

# TEST_6:
superint = SuperInt(30)

for i in range(10):
    superint = superint.next()
    print(superint)

# TEST_7:
superint = SuperInt(30)

for i in range(10):
    superint = superint.prev()
    print(superint)

# TEST_8:
superint = SuperInt(50)

for i in range(0, 50, 3):
    superint = superint.next()
    print(superint.to_bin())

# TEST_9:
superint = SuperInt(-200)

for i in range(0, 100, 3):
    superint = superint.next()
    print(superint.to_bin())

# TEST_10:
superint = SuperInt(50)

for i in range(0, 50, 3):
    superint = superint.next()
    print(*superint)

# TEST_11:
superint = SuperInt(-200)

for i in range(0, 100, 3):
    superint = superint.next()
    print(*superint)

# TEST_12:
superint = SuperInt(100)
print(type(superint))
print(type(superint.next()))
print(type(superint.prev()))
print(type(superint.repeat()))

# TEST_13:
superint1 = SuperInt(2023)

for item in superint1:
    print(item, type(item))
