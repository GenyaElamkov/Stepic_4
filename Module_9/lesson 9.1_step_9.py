class TicTacToe:
    def __init__(self) -> None:
        self.game_board = [[" "] * 3 for _ in range(3)]
        self._flag = True

    def mark(self, row, col):
        if self.winner():
            print("Игра окончена")
            return

        if self.game_board[row - 1][col - 1] == ("X" or "O"):
            print("Недоступная клетка")
            return

        if self._flag:
            self.game_board[row - 1][col - 1] = "X"
            self._flag = False
        else:
            self.game_board[row - 1][col - 1] = "O"
            self._flag = True

    def _gorizont(self):
        for row in self.game_board:
            game_x = map(lambda x: x == "X", row)
            game_o = map(lambda x: x == "O", row)

            if all(game_x):
                return "X"
            if all(game_o):
                return "O"

    def _vertical(self):
        for row in tuple(zip(*self.game_board)):
            game_x = map(lambda x: x == "X", row)
            game_o = map(lambda x: x == "O", row)

            if all(game_x):
                return "X"
            if all(game_o):
                return "O"

    def _diagonal(self):
        diag_base = diag_side = []
        for i in range(len(self.game_board)):
            diag_base.append(self.game_board[i][i])
            diag_side.append(self.game_board[i][len(self.game_board) - i - 1])

        if all(map(lambda x: x == "X", diag_base)):
            return "X"
        if all(map(lambda x: x == "O", diag_side)):
            return "O"

    def winner(self):
        for res in (self._gorizont(), self._vertical(), self._diagonal()):
            if res is not None:
                return res

        _cnt = 0
        for row in self.game_board:
            for col in row:
                if col == "X" or col == "O":
                    _cnt += 1

        if _cnt == 9:
            return "Ничья"

    def show(self):
        for i, row in enumerate(self.game_board):
            print("|".join(row))
            if i < 2:
                print("-" * 5)


# INPUT DATA:

# # TEST_1:
# tictactoe = TicTacToe()

# tictactoe.mark(1, 1)
# tictactoe.mark(3, 1)
# tictactoe.mark(1, 1)

# tictactoe.mark(1, 3)
# tictactoe.mark(1, 2)
# tictactoe.mark(3, 3)
# tictactoe.mark(2, 2)
# tictactoe.mark(2, 3)

# print(tictactoe.winner())
# tictactoe.mark(2, 1)
# tictactoe.show()

# # TEST_2:
# tictactoe = TicTacToe()

# tictactoe.mark(1, 1)
# tictactoe.mark(3, 2)
# tictactoe.mark(1, 1)

# tictactoe.mark(1, 3)
# tictactoe.mark(1, 2)
# tictactoe.mark(3, 3)
# tictactoe.mark(2, 2)
# tictactoe.mark(2, 3)

# print(tictactoe.winner())
# tictactoe.show()

# # TEST_3:
# tictactoe = TicTacToe()

# tictactoe.mark(1, 1)
# tictactoe.mark(3, 2)
# tictactoe.mark(1, 3)
# tictactoe.mark(1, 2)
# tictactoe.mark(3, 3)
# tictactoe.mark(2, 3)
# tictactoe.mark(3, 1)
# tictactoe.mark(2, 1)
# tictactoe.mark(2, 2)

# print(tictactoe.winner())
# tictactoe.show()
# tictactoe.mark(2, 2)

# TEST_4:
tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(1, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)

print(tictactoe.winner())

tictactoe.mark(3, 2)
tictactoe.mark(3, 3)
tictactoe.mark(1, 2)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)
print(tictactoe.winner())
