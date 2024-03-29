

import itertools


clav = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "@", "0", "&"]
wimdow = ["6", "7", "&", "8", "2", "3", "4", "5", "0", "9", "@", "1"]

d = dict(zip(clav, wimdow))

keys, values = zip(*d.items())
permutations_dicts = [dict(zip(keys, v)) for v in itertools.product(*values)]
print(permutations_dicts)
# print(d)
# comb = []
# cnt = 0
# start = []
# flag = True
# while flag:
#     for k in d.keys():
#         for key, v in d.items():
#             if k == v:
#                 cnt += 1
#                 comb.append(key)
#                 start.append(k)
#             if cnt == 5:
#                 print(comb)
#                 if set(start) == set(comb):
#                     flag = False
#                     break
#                 # else:
#                 #     cnt = 0
#         if not flag:
#             break
#     if  not flag:
#         break

# print(comb)
# while True:
#     for k in d.keys():
#         print(k)
#         break
#         # for v in d.values():
#         #     print(v)
#         # if k == v:
#         #     comb.append(k)
#         #     cnt += 1
#     break
#     if cnt == 1:
#         break


# print(comb)
