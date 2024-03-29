# for i in range(1, 51):
#     if(i % 2 != 0 & i % 3 != 0):
#         print(i)




# def check_divisibility(x):
#     return (x % 2 != 0) and (x % 3 != 0) and (x % 5 != 0)


# range_obj = range(1, num + 1)

# filtered_nums = list(filter(check_divisibility, range_obj))
# print(len(filtered_nums))

# cnt = 0 
# for i in range(1, num+1, 2):
     
#     if i % 3 != 0 and i % 5 != 0:
#         cnt += 1

# print(cnt)
num = int(input())

# result = sum(1 for x in range(1, num+1,2) if  x % 3 != 0 and x % 5 != 0 and x % 30 != 0)
# # print(sum(1 for _ in result))
# print(result)


p = lambda n: sum(i+j for i in range(n) for j in range(2*n))
print(p(num))