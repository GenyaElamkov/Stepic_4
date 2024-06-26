class ArithmeticProgression:
    def __init__(self, start, diff) -> None:
        self.start = start
        self.diff = diff

    def __iter__(self):
        res = self.start
        while True:
            yield res
            res += self.diff


class GeometricProgression(ArithmeticProgression):
    def __iter__(self):
        res = self.start
        while True:
            yield res
            res *= self.diff



# INPUT DATA:

# # TEST_1:
# progression = ArithmeticProgression(0, 1)

# for elem in progression:
#     if elem > 10:
#         break
#     print(elem, end=' ')

# # TEST_2:
# progression = GeometricProgression(1, 2)

# for elem in progression:
#     if elem > 10:
#         break
#     print(elem, end=' ')

# # TEST_3:
# progression = GeometricProgression(4, -2)
# count = 0

# for item in progression:
#     if count == 20:
#         break
#     count += 1
#     print(item, end=' ')

# # TEST_4:
# progression = ArithmeticProgression(100, -10)
# count = 0

# for item in progression:
#     if count == 20:
#         break
#     count += 1
#     print(item, end=' ')

# TEST_5:
progression = GeometricProgression(100, 10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')