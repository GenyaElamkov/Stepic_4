from collections import UserList

class DefaultList(UserList):
    def __init__(self, iterable=[], default=None):
        super().__init__(iterable)
        self.default = default

    def __getitem__(self, index):
        try:
            return self.data[index]
        except IndexError:
            return self.default

    # def __setitem__(self, index, item):
    #     self.data[index] = item


# INPUT DATA:

# # TEST_1:
# defaultlist = DefaultList([1, 2, 3])

# print(defaultlist[0])
# print(defaultlist[-1])
# print(defaultlist[100])
# print(defaultlist[-100])

# # TEST_2:
# defaultlist = DefaultList([1, 2, 3], 0)

# print(defaultlist[0])
# print(defaultlist[-1])
# print(defaultlist[100])
# print(defaultlist[-100])

# # TEST_3:
# defaultlist = DefaultList()

# print(defaultlist)

# TEST_4:
data = [1, 2, 3]
defaultlist = DefaultList(data)

print(defaultlist)
data.extend([4, 5, 6])
print(data)
print(defaultlist)

# # TEST_5:
# defaultlist = DefaultList(default='empty result')

# print(defaultlist[100])
# print(defaultlist[1000])
# print(defaultlist[10000])

# # TEST_6:
# digits = [184, 79, 154, 112, 85, 39, 126, 50, 111, 125, 148, 100, 187, 28, 90, 83, 156, 51, 142, 183, 94, 86, 68, 111,
#           163, 189, 94, 112, 139, 134, 81, 182, 62, 173, 97, 36, 54, 128, 21, 165, 197, 103, 76, 84, 84, 120, 112, 184,
#           68, 36]

# indexes = [7940, 43, 4255, 1368, 8924, 28, 35, 7048, 6054, 0, 3982, 6224, 6614, 4189, 37, 38, 15, 2712, 22, 38, 8, 33,
#            5883, 3561, 45, 36, 15, 8, 17, 32, 2088, 31, 47, 7888, 19, 4793, 3237, 8751, 18, 21, 1888, 2999, 17, 2027,
#            5611, 4380, 33, 6279, 1383, 1, 41, 45, 7622, 9479, 30, 37, 2855, 32, 5233, 5869, 33, 10, 7387, 11, 9104, 8,
#            15, 27, 50, 29, 44, 41, 4462, 8661, 13, 6736, 3588, 48, 1, 7175, 2, 3955, 42, 5677, 6835, 1436, 5102, 3833,
#            45, 35, 32, 2374, 33, 4210, 3280, 41, 11, 1503, 8688, 2941, 4945]

# defaultlist = DefaultList(digits, default='empty result')

# for index in indexes:
#     print(defaultlist[index])

# # TEST_7:
# defaultlist = DefaultList([1, 2, 3])
# print(defaultlist[-1])
# print(defaultlist[-2])
# print(defaultlist[-3])