

# 61570068
# 1617462603
def even_odd_sums(sequence):
    return sum(i for i in sequence[::2]) - sum(i for i in sequence[1::2])

# res = range(int(input()), int(input())+1)
# print(even_odd_sums(res))

# even = odd = 0
# for num in iter(res):
#     if num % 2 == 0:
#         even += num
#     else:
#         odd += num
# print(even - odd)

a = int(input())
b = int(input())
a2 = a + a % 2
b2 = b - b % 2
even = (b2 + a2) // 2 * ((b2 - a2) // 2 + 1)
a1 = a + (1 - a % 2)
b1 = b - (1 - b % 2)
odd = (b1 + a1) // 2 * ((b1 - a1) // 2 + 1)
print(even - odd)