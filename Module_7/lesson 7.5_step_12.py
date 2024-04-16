from abc import ABC, abstractclassmethod


class ChessPiece(ABC):
    def __init__(self, horizontal: str, vertical: int) -> None:
        self.horizontal = ord(chr(horizontal) - 96)
        self.vertical = vertical

    @abstractclassmethod
    def can_move(self):
        raise NotImplementedError


class King(ChessPiece):
    def can_move(self, h: str, v: int):
        # horiz_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        
        d = {"a" :1, "b" :2, "c" :3, "d" :4, "e" :5, "f" :6,"g" :7, "h" : 8}
        fir, sec = input(), input()
        print(d[a[0]])
        f1, f2, s1, s2 = d[fir[0]], int(fir[1]), d[sec[0]], int(sec[1])
        if abs(f1 - s1) in [0, 1] and abs(f2 - s2) in [0, 1]:
            print("YES")
        else:
            print("NO")

        # self.horizontal = int(input())  # Column number of the first cell
        # self.vertical = int(input())  # Row number of the first cell
        # x1 = int(input())  # Column number of the second cell
        # y1 = int(input())  # Row number of the second cell

        # h = ord(chr(h) - 96)

        # if (1 >= h-self.horizontal >= -1) and (1 >= v-self.vertical >= -1):
        #     print('YES')
        # else:
        #     print('NO')


# class Knight(ChessPiece):
#     def can_move(self, horizontal: str, vertical: int):
#         possible_moves = [
#             [horizontal + 2, vertical + 1], [horizontal + 2, vertical - 1],
#             [horizontal - 2, vertical + 1], [horizontal - 2, vertical - 1],
#             [horizontal + 1, vertical + 2], [horizontal + 1, vertical - 2],
#             [horizontal - 1, vertical + 2], [horizontal - 1, vertical - 2]
#         ]


# INPUT DATA:

# TEST_1:
king = King('b', 2)

print(king.can_move('c', 3))
print(king.can_move('a', 1))
print(king.can_move('f', 7))

# # TEST_2:
# knight = Knight('c', 3)

# print(knight.can_move('e', 5))
# print(knight.can_move('e', 4))

# # TEST_3:
# king = King('e', 3)

# print(king.can_move('e', 3))
# print(king.can_move('e', 4))
# print(king.can_move('b', 1))

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

# # TEST_7:
# kings = [King(h, v) for h in 'abcdefgh' for v in range(1, 9)]

# for king in kings:
#     print('*' * 20)
#     for horizontal in 'abcdefgh':
#         for vertical in range(1, 9):
#             if king.can_move(horizontal, vertical):
#                 print(f'King({king.horizontal}{king.vertical})', f'{horizontal}{vertical}',
#                       king.can_move(horizontal, vertical))

# # TEST_8:
# knights = [Knight(h, v) for h in 'abcdefgh' for v in range(1, 9)]

# for knight in knights:
#     print('*' * 20)
#     for horizontal in 'abcdefgh':
#         for vertical in range(1, 9):
#             if knight.can_move(horizontal, vertical):
#                 print(f'Knight({knight.horizontal}{knight.vertical})', f'{horizontal}{vertical}',
#                       knight.can_move(horizontal, vertical))