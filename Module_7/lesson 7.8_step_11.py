from random import shuffle


class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return "".join(map(str, [self.suit, self.rank]))


class Deck:
    _ranks = [str(n) for n in list(range(2, 11)) + ["J", "Q", "K", "A"]]
    _suits = "♣ ♢ ♡ ♠".split()

    def __init__(self) -> None:
        self.cards = [Card(suit, rank) for suit in self._suits for rank in self._ranks]

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Перемешивать можно только полную колоду")
        shuffle(self.cards)

    def deal(self):
        if not self.cards:
            raise ValueError("Все карты разыграны")
        return self.cards.pop()

    def __str__(self) -> str:
        return f"Карт в колоде: {len(self.cards)}"


# INPUT DATA:

# # TEST_1:
# print(Card('♣', '4'))
# print(Card('♡', 'A'))
# print(Card('♢', '10'))

# # TEST_2:
# deck = Deck()

# print(deck)
# print(deck.deal())
# print(deck.deal())
# print(deck.deal())
# print(type(deck.deal()))
# print(deck)

# # TEST_3:
# deck = Deck()

# for _ in range(52):
#     deck.deal()

# try:
#     deck.deal()
# except ValueError as error:
#     print(error)

# TEST_4:
# deck = Deck()

# deck.deal()

# try:
#     deck.shuffle()
# except ValueError as error:
#     print(error)

# # TEST_5:
# deck = Deck()

# for _ in range(52):
#     print(deck.deal())

# TEST_6:
deck = Deck()

deck.shuffle()

for _ in range(52):
    print(deck.deal())
