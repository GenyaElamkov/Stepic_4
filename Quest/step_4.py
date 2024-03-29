# A, B, C, D, A × B, B × C, C × D, D × A

# res = list(map(int, "2 5 20 21 10 100 420 42".split()))
# res = sorted(map(int, "7 217 15 589 31 105 19 285".split()))
# res = sorted(map(int, "2 6 7 3 14 35 15 5".split()))
# print(res)

# cd = res[-1]
# c = sorted(set(res))[2]
# for i in range(len(res) - 1):
#     for j in range(i, len(res) - 1):
#         if res[i] * res[j] == res[-1] or :
#             print(res[j])
#             break

# print(cd // c)

# res = sorted(map(int, "2 5 20 21 10 100 420 42".split()))
# print(res)
# arr_1 = []
# arr_2 = []
# arr_1.extend(res[:4])
# arr_2.extend(res[4:])
# print(arr_2)
# cnt = 0
# for i, v in enumerate(res[:4]):
#     if arr_1[i- 1] * arr_1[i] in arr_2:
#         print('wrwr')
#         cnt += 1
#     else:
#         print('Nen')
#         print(arr_2)
#     if cnt > 4:
#         print('No')


# for i in range(len(res) - 1):
#     for j in range(len(res) - 1 - i):
#         if res[j] > res[j + 1]:
#             res[j], res[j + 1] = res[j + 1], res[j]


# arr = map(int, "2 5 20 21 10 100 420 42".split())
arr = list(map(int, "2 3 4 1 12 6 2 4".split()))
a, b, c, d, ab, bc, cd, da = arr
if a * b == ab and b * c == bc and c * d == cd and d * a == da:
    print(d)
arr = sorted(arr)

if a < b < c < d:
    print(True)
while True:
    for i, v in enumerate(arr):
        if arr[i-1] == arr[i]:
            r = arr.pop(v)
            print(r)

