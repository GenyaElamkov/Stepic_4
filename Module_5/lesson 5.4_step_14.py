class Matrix:
    def __init__(self, rows, cols, value=0) -> None:
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __str__(self) -> str:
        res = ""
        for row in self.matrix:
            for col in row:
                res += str(col) + " "
            res = res[:-1] + "\n"
        return res[:-1]

    def __repr__(self) -> str:
        return f"{__class__.__name__}{self.rows, self.cols}"

    def __pos__(self):
        new_matrix = __class__(self.rows, self.cols, self.value)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(i, j, self.get_value(i, j))
        return new_matrix

    def __neg__(self):
        new_matrix = +self
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_value(i, j, -self.get_value(i, j))
        return new_matrix

    def __invert__(self):
        new_matrix = __class__(self.cols, self.rows, self.value)
        new_matrix.matrix = list(map(list, zip(*self.matrix)))
        return new_matrix

    def __round__(self, n=0):
        new_matrix = __class__(self.rows, self.cols, self.value)
        for row in range(self.rows):
            for col in range(self.cols):
                new_matrix.set_value(row, col, round(self.get_value(row, col), n))
        return new_matrix


# class Matrix:
#     def __init__(self, rows, cols, value=0):
#         self.rows = rows
#         self.cols = cols
#         self.matrix = [[value] * cols for _ in range(rows)]

#     def get_value(self, row, col):
#         return self.matrix[row][col]

#     def set_value(self, row, col, value):
#         self.matrix[row][col] = value

#     def copy(self, func=lambda x: x, transpose=False):
#         if transpose:
#             matrix = Matrix(self.cols, self.rows)
#         else:
#             matrix = Matrix(self.rows, self.cols)
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 value = func(self.get_value(row, col))
#                 if transpose:
#                     matrix.set_value(col, row, value)
#                 else:
#                     matrix.set_value(row, col, value)
#         return matrix

#     def __str__(self):
#         rows = (" ".join(map(str, row)) for row in self.matrix)
#         return "\n".join(rows)

#     def __repr__(self):
#         return f"Matrix({self.rows}, {self.cols})"

#     def __pos__(self):
#         return self.copy()

#     def __neg__(self):
#         return self.copy(func=lambda x: -x)

#     def __invert__(self):
#         return self.copy(transpose=True)

#     def __round__(self, n=0):
#         return self.copy(func=lambda x: round(x, n))


matrix = Matrix(2, 3, 1)

print(matrix)
print()
print(~matrix)


matrix = Matrix(2, 3, 1)

plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(plus_matrix.cols, plus_matrix.rows)
print(minus_matrix.cols, minus_matrix.rows)
print(invert_matrix.cols, invert_matrix.rows)
