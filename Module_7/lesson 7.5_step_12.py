from abc import ABC, abstractclassmethod


class ChessPiece(ABC):
    def __init__(self, horizontal: str, vertical: int) -> None:
        self.horizontal = horizontal
        self.vertical = vertical
        self._horizontal_num = ord(horizontal) - 96

    @abstractclassmethod
    def can_move(self):
        raise NotImplementedError


class King(ChessPiece):
    def can_move(self, h: str, v: int):
        h = ord(h) - 96
        if self._horizontal_num == h and self.vertical == v:
            return False
        if (1 >= h - self._horizontal_num >= -1) and (1 >= v - self.vertical >= -1):
            return True
        return False


class Knight(ChessPiece):
    def can_move(self, h: str, v: int):
        h = ord(h) - 96
        if (
            (h - self._horizontal_num) * (h - self._horizontal_num)
            + (v - self.vertical) * (v - self.vertical)
            == 5
            and 0 <= h <= 8
            and 0 <= v <= 8
        ):
            return True
        return False


# INPUT DATA:

# # TEST_1:
# king = King('b', 2)

# print(king.can_move('c', 3))
# print(king.can_move('a', 1))
# print(king.can_move('f', 7))

# # TEST_2:
# knight = Knight('c', 3)

# print(knight.can_move('e', 5))
# print(knight.can_move('e', 4))

# # TEST_3:
# king = King("e", 3)

# print(king.can_move("e", 3))
# print(king.can_move("e", 4))
# print(king.can_move("b", 1))

# # TEST_4:
# knight = Knight('h', 8)

# print(knight.can_move('h', 8))
# print(knight.can_move('a', 6))
# print(knight.can_move('a', 1))
# print(knight.can_move('g', 6))

# # TEST_5:
# knight = Knight('a', 1)

# for horizontal in 'abcdefg':
#     for vertical in range(1, 9):
#         print(f'{horizontal}{vertical}', knight.can_move(horizontal, vertical))

# # TEST_6:
# king = King('a', 1)

# for horizontal in 'abcdefg':
#     for vertical in range(1, 9):
#         print(f'{horizontal}{vertical}', king.can_move(horizontal, vertical))

# TEST_7:
kings = [King(h, v) for h in "abcdefgh" for v in range(1, 9)]

for king in kings:
    print("*" * 20)
    for horizontal in "abcdefgh":
        for vertical in range(1, 9):
            if king.can_move(horizontal, vertical):
                print(
                    f"King({king.horizontal}{king.vertical})",
                    f"{horizontal}{vertical}",
                    king.can_move(horizontal, vertical),
                )

# # TEST_8:
# knights = [Knight(h, v) for h in "abcdefgh" for v in range(1, 9)]

# for knight in knights:
#     print("*" * 20)
#     for horizontal in "abcdefgh":
#         for vertical in range(1, 9):
#             if knight.can_move(horizontal, vertical):
#                 print(
#                     f"Knight({knight.horizontal}{knight.vertical})",
#                     f"{horizontal}{vertical}",
#                     knight.can_move(horizontal, vertical),
#                 )
