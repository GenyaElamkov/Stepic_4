x, y = input()

n = 8
matrix = [['.'] * n for _ in range(n)]
y = n - int(y)
x = ord(x) - 97
print(x)
matrix[y][x] = 'N'

for i in range(n):
    for j in range(n):
        if abs(i - y) * abs(j - x) == 2:
            matrix[i][j] = '*'

for x in range(n):
    print(*matrix[x], sep='')
