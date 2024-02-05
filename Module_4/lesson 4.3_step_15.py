class Wordplay:
    def __init__(self, words: list[str] = []) -> None:
        self.words = words[:]

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int) -> list[str]:
        return [word for word in self.words if len(word) == n]

    def only(self, *args) -> list[str]:
        arr = []
        for word in self.words:
            for c in word:
                if c not in args:
                    break
            else:
                arr.append(word)
        return arr

    def avoid(self, *args) -> list[str]:
        arr = []
        for word in self.words:
            for c in word:
                if c in args:
                    break
            else:
                arr.append(word)
        return arr


words = ["Лейбниц", "Бэббидж", "Нейман", "Джобс", "да_Винчи", "Касперский"]
wordplay = Wordplay(words)

words.extend(["Гуев", "Харисов", "Светкин"])
print(words)
print(wordplay.words)
