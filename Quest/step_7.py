# num = 2338

cnt = 0
num = 0
one = 1
while cnt < 2338:
    num += 1
    arr = list(map(int, list(str(num))))
    if one in arr:
        cnt += arr.count(one)



print(num, cnt)


