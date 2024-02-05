class Knight:

    def __init__(self, horizontal: str, vertical: int, color: str) -> None:
        self.horizontal = horizontal
        self.horizontal_num = ord(horizontal) - 97
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return "N"

    def can_move(self, horizontal: str, vertical: int) -> bool:
        horizontal_num = ord(horizontal) - 97
        if (
            (horizontal_num - self.horizontal_num)
            * (horizontal_num - self.horizontal_num)
            + (vertical - self.vertical) * (vertical - self.vertical)
            == 5
            and 0 <= horizontal_num <= 8
            and 0 <= vertical <= 8
        ):
            return True
        return False

    def move_to(self, horizontal: str, vertical: int) -> None:
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.horizontal_num = ord(horizontal) - 97
            self.vertical = vertical

    def draw_board(self) -> None:
        for vertical in range(8, 0, -1):
            for horizontal in "abcdefgh":
                if self.can_move(horizontal, vertical):
                    print("*", end="", sep="")
                elif vertical == self.vertical and horizontal == self.horizontal:
                    print(self.get_char(), sep="", end="")
                else:
                    print(".", end="", sep="")
            print()


# knight_1 = Knight('c', 3, 'white')

# print(knight_1.color, knight_1.get_char())
# print(knight_1.horizontal, knight_1.vertical)

# knight_2 = Knight("c", 3, "white")

# print(knight_2.horizontal, knight_2.vertical)
# print(knight_2.can_move("e", 5))
# print(knight_2.can_move("e", 4))

# knight_2.move_to("e", 4)
# print(knight_2.horizontal, knight_2.vertical)


knight_3 = Knight("c", 3, "white")
knight_3.draw_board()

# knight_4 = Knight("e", 5, "black")

# knight_4.draw_board()
# knight_4.move_to("d", 3)
# # print(knight_4.horizontal)
# print()
# knight_4.draw_board()


# knight_5 = Knight('a', 1, 'white')

# knight_5.draw_board()
# knight_5.move_to('e', 8)
# print()
# knight_5.draw_board()
