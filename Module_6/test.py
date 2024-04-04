res = []
if not res:
    res.append([5])


res[-1].append(1)
res[-1][-1].append([2])
res[-1][-1][-1].append([3])
res[-1][-1][-1][-1].append([4])


res.append([5])


print(res)

