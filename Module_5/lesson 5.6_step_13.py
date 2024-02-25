class Strip:
    def __init__(self, chars) -> None:
        self.chars = chars

    def __call__(self, string: str):
        return string.strip(self.chars)

strip = Strip('!? ')

print(strip('     ?beegeek!'))
print(strip('!bee?geek!'))