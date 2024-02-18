from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word) -> None:
        self.word = word

    def __str__(self) -> str:
        return self.word.title()

    def __repr__(self) -> str:
        return f"{__class__.__name__}('{self.word}')"

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return len(self.word) == len(__value.word)
        return NotImplemented

    def __lt__(self, __value):
        if isinstance(__value, __class__):
            return len(self.word) < len(__value.word)
        return NotImplemented


print(Word("bee") == Word("hey"))
print(Word("bee") < Word("geek"))
print(Word("bee") > Word("geek"))
print(Word("bee") <= Word("geek"))
print(Word("bee") >= Word("gee"))

words = [Word("python"), Word("bee"), Word("geek")]

print(sorted(words))
print(min(words))
print(max(words))
