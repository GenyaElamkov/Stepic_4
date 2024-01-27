"""
Дартс
Будем считать, что игровое поле для игры в дартс представляет собой квадратную матрицу, заполненную натуральными числами, расположенными в порядке возрастания от краев к центру. Стороной игрового поля будем называть сторону квадратной матрицы, которую представляет это поле.

Напишите программу, которая создает поле для игры в дартс определенного размера.

Формат входных данных
На вход программе подается единственное натуральное число — сторона игрового поля.

Формат выходных данных
Программа должна создать и вывести игровое поле с заданной стороной.

Примечание 1. Гарантируется, что сторона игрового поля не превышает 18.

https://stepik.org/lesson/794484/step/4?unit=797232
"""

size = 5

matrix = [[1] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        if size <= 2:
            matrix[i][j] = 1

        if i == size - i - 1 and j == size - j - 1:
            matrix[i][j] = size - i


        if i == j + 1 or  j == i + 1:
            matrix[i][j] = size - j

        # if i < j and size - 1 - j:
        #     matrix[i][j] = 2

        # if i > j and size - 1 - j:
        #     matrix[i][j] = size - i

        # if i < j and i > size - 1 - j:
        #     matrix[i][j] = 2

        # if i > j and i > size - 1 - j:
        #     matrix[i][j] = 2

        # if j == size - 1 - i:
        #     matrix[i][j] = 1
        # if i == j or j == size - i - 1:
        #     matrix[i][j] = 2

        # if i + 1 == size - i:
        #     matrix[i][j] = size - i
        
        # if j + 1 == size - l:
        #     matrix[i][j] = size - i
            
    


for row in matrix:
    print(*row)
