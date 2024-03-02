def hash_function(obj):
    obj = str(obj)
    tmp_1 = 0
    for i, _ in enumerate(obj):
        if i == len(obj) // 2 and len(obj) % 2 == 0:
            break
        if i == len(obj) // 2 and len(obj) % 2 == 1:
            tmp_1 += ord(obj[i])
            break
        tmp_1 += ord(obj[i]) * ord(obj[-(i + 1)])

    tmp_2 = 0
    for i, _ in enumerate(obj):
        tmp_2 += ord(obj[i]) * (i + 1) * (-1) ** i

    return (tmp_1 * tmp_2) % 123456791


# print(hash_function(12345))  # 5248 # 159
# print(hash_function('python')) #-303

print(hash_function(None))
