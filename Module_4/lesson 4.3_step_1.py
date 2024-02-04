class PyggyBank:
    """Копилка"""

    def __init__(self, balance=0, volume=400) -> None:
        self.balance = balance  # кол-во монетв в копилке
        self.volume = volume  # вместимость копилки

    def add_coins(self, coins):
        """Добовляет монету."""
        if self.balance + coins > self.volume:
            raise ValueError("Копилка слишком мала")
        self.balance += coins

    def remove_coins(self, coins):
        """Уменьшает монету."""
        if self.volume - coins < 0:
            raise ValueError('В копилке недостаточно монет')
        self.balance -= coins


piggybank = PyggyBank(100)
print(piggybank.balance)

piggybank.add_coins(300)
print(piggybank.balance)

piggybank.remove_coins(450)
print(piggybank.balance)
