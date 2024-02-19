class Money:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.amount} руб."

    def __pos__(self) -> object:
        return __class__(abs(self.amount))

    def __neg__(self) -> object:
        return __class__(-abs(self.amount))


money = Money(-100)

print(money)
print(+money)
print(-money)

money = Money(100)

print(money)
print(+money)
print(-money)
