class TextHandler:
    def __init__(self) -> None:
        self.words = []

    def add_words(self, text: str):
        return self.words.extend(text.split())

    def get_shortest_words(self):
        if not self.words:
            return self.words
        min_len_word = len(min(self.words, key=len))
        return [x for x in self.words if min_len_word == len(x)]

    def get_longest_words(self):
        if not self.words:
            return self.words
        max_len_word = len(max(self.words, key=len))
        return [x for x in self.words if max_len_word == len(x)]


texthandler = TextHandler()

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())


texthandler = TextHandler()

texthandler.add_words("do not be sorry")
texthandler.add_words("be")
texthandler.add_words("better")

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
