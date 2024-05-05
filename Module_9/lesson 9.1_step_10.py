from random import shuffle


class Game:
    def __init__(self, rows, cols, mines) -> None:
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell(i, j) for j in range(cols)] for i in range(rows)]
        self.set_mine()
        self.get_mine()

    def set_mine(self):
        self._mines = list(range(1, self.rows * self.cols + 1))
        shuffle(self._mines)
        self._mines = self._mines[: self.mines]
        cnt = 0
        for i, row in enumerate(self.board):
            for j, _ in enumerate(row):
                cnt += 1
                if cnt in self._mines:
                    self.board[i][j].mine = True

    def get_mine(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cnt_mine = 0
                for row_dx in [-1, 0, 1]:
                    for col_dx in [-1, 0, 1]:
                        if 0 <= i + row_dx < self.rows and 0 <= j + col_dx < self.cols:
                            if self.board[i + row_dx][j + col_dx].mine:
                                cnt_mine += 1
                self.board[i][j].neighbours = cnt_mine
                if self.board[i][j].mine and cnt_mine > 0:
                    self.board[i][j].neighbours -= 1

    def __str__(self):
        print(*self.board, sep="\n")
        return ""


class Cell:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.mine = False
        self.neighbours = 0

    def __repr__(self):
        return f"{self.mine}|{self.neighbours}"


# INPUT DATA:

# TEST_1:
game = Game(14, 18, 40)
print(game.rows)
print(game.cols)
print(game.mines)

cell = game.board[0][0]

print(cell.row)
print(cell.col)
print(0 <= cell.neighbours <= 3)

# TEST_2:
game = Game(10, 8, 14)

for r, c in ((0, 0), (0, -1), (-1, 0), (-1, -1)):
    cell = game.board[r][c]
    print(0 <= cell.neighbours <= 3, type(cell))

# TEST_3:
game = Game(10, 8, 14)

for r in (0, -1):
    for c in range(1, game.cols - 1):
        cell = game.board[r][c]
        print(0 <= cell.neighbours <= 5, type(cell))

# TEST_4:
game = Game(10, 8, 14)

for c in (0, -1):
    for r in range(1, game.rows - 1):
        cell = game.board[r][c]
        print(0 <= cell.neighbours <= 5, type(cell))

# TEST_5:
n, m = 10, 8
game = Game(n, m, 14)
total_mines = 0

for r in range(n):
    for c in range(m):
        if not game.board[r][c].mine:
            print(get_neighbours_count(r, c, game) == game.board[r][c].neighbours)
        total_mines += game.board[r][c].mine


print(total_mines == game.mines)
print(total_mines)
print(game.mines)
