n = int(input())
nums = range(0, 10**12)
s = 0
while n:
    s += n % 10
    n //= 10

print(s)
