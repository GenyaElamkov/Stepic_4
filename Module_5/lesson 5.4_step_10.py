class ReversibleString:
    def __init__(self, string) -> None:
        self.string = string

    def __str__(self) -> str:
        return self.string

    def __neg__(self):
        return __class__(self.string[::-1])


string = ReversibleString("python")

print(string)
print(-string)


string = ReversibleString("beegeek")

print(-string)
print(type(-string))
