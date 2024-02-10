from string import punctuation, digits, whitespace


class StrExtension:
    @staticmethod
    def remove_vowels(string: str) -> str:
        chars = "aeiouyAEIOUY"
        return string.translate({ord(i): None for i in chars})

    @staticmethod
    def leave_alpha(string: str) -> str:
        return string.translate({ord(i): None for i in punctuation + digits + whitespace})

    @staticmethod
    def replace_all(string, chars, char) -> str:
        return string.translate({ord(i): char for i in chars})


print(StrExtension.remove_vowels("Python"))
print(StrExtension.remove_vowels("Stepik"))
print(StrExtension.leave_alpha("Python111"))
print(StrExtension.leave_alpha("__Stepik__()"))

print(StrExtension.replace_all("Python", "Ptn", "-"))
print(StrExtension.replace_all("Stepik", "stk", "#"))
print(StrExtension.leave_alpha('beegeek!\"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~BEEGEEK'))
print(StrExtension.leave_alpha('beegeek0123456789BEEGEEK'))