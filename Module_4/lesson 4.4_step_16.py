from typing import Type


class BankAccount:
    def __init__(self, balance: int | float = 0) -> None:
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount: int | float) -> None:
        self._balance += amount

    def withdraw(self, amount: int | float) -> None | ValueError:
        if self._balance - amount < 0:
            raise ValueError("На счете недостаточно средств")
        self._balance -= amount

    def transfer(self, account: Type["BankAccount"], amount: int | float) -> None:
        self.withdraw(amount)
        account.deposit(amount)


account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)
