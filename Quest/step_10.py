# result = 0
# for i in range(n):
#     for j in range(2*n):
#         result += j + i

# n = int(input())
# result = 0
# for i in range(n):
#     result += n * (2 * n - 1) + (n * (n - 1)) // 2
# print(result)


# print(sum((j + i for i in range(n) for j in range(2 * n)), 0))


# result = 0
# for i in range(n):
#     result += (2 * n) * n + (n * (n-1)) // 2


# for i in range(1, n + 1):
#     q = 1 / ((i + 1) * (i + 1))
#     t = 1
#     for k in range(1, 2 * n + 1):
#         t *= q
#         result += t / k


# def ver1():
#     r = [Score[j][a[j]] for j in range(40)]
#     for i in xrange(100000):
#         total = 0
#         for j in r:
#             total+=j
#     print (total)

# def ver2():
#     r = [Score[j][a[j]] for j in xrange(40)]
#     for i in xrange(100000):
#         total = sum(r)
#     print (total)


number = 5
x=0
for i in range(0, 5000):
    x += number//10**i
print(x)