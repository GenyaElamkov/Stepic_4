from string import ascii_lowercase, ascii_uppercase


class CaesarCipher:
    def __init__(self, shift) -> None:
        self.shift = shift
        self._ascii_lowercase = ascii_lowercase
        self._ascii_uppercase = ascii_uppercase

    def encode(self, text):
        arr = []
        for char in text:
            if char in self._ascii_lowercase:
                res = self._ascii_lowercase[
                    (self._ascii_lowercase.index(char) + self.shift) % 26
                ]
            elif char in self._ascii_uppercase:
                res = self._ascii_uppercase[
                    (self._ascii_uppercase.index(char) + self.shift) % 26
                ]
            else:
                res = char
            arr.append(res)

        return "".join(arr)

    def decode(self, text):
        arr = []
        for char in text:
            if char in self._ascii_lowercase:
                res = self._ascii_lowercase[
                    (self._ascii_lowercase.index(char) - self.shift) % 26
                ]

            elif char in self._ascii_uppercase:
                res = self._ascii_uppercase[
                    (self._ascii_uppercase.index(char) - self.shift) % 26
                ]
            else:
                res = char
            arr.append(res)

        return "".join(arr)

# from string import ascii_lowercase as low, ascii_uppercase as up


# class CaesarCipher:
#     def __init__(self, key):
#         self._encode = str.maketrans(low, low[key:] + low[:key]) | str.maketrans(up, up[key:] + up[:key])
#         self._decode = {v: k for k, v in self._encode.items()}

#     def encode(self, string):
#         return str.translate(string, self._encode)

#     def decode(self, string):
#         return str.translate(string, self._decode)



# INPUT DATA:

# # TEST_1:
# cipher = CaesarCipher(10)

# print(cipher.encode('Beegeek'))
# print(cipher.decode('Gjjljjp'))


# # # TEST_2:
# cipher = CaesarCipher(5)

# print(cipher.encode('Биgeek123'))
# print(cipher.decode('Биljjp123'))

# # TEST_3:
# cipher = CaesarCipher(10)

# words = [
#     "leader",
#     "life",
#     "central",
#     "whatever",
#     "true",
#     "show",
#     "year",
#     "teacher",
#     "happen",
#     "might",
#     "defense",
#     "suggest",
#     "boy",
#     "trip",
#     "wish",
#     "interest",
#     "star",
#     "system",
#     "husband",
#     "wait",
#     "young",
#     "certainly",
#     "with",
#     "wind",
#     "thought",
#     "hard",
#     "today",
#     "cup",
#     "where",
#     "fly",
#     "agreement",
#     "human",
#     "decision",
#     "along",
#     "billion",
#     "prevent",
#     "authority",
#     "those",
#     "do",
#     "perform",
#     "plan",
#     "allow",
#     "president",
#     "do",
#     "around",
#     "seven",
#     "dog",
#     "sea",
#     "use",
#     "my",
#     "head",
#     "whose",
#     "important",
#     "top",
#     "current",
#     "east",
#     "page",
#     "decide",
#     "mouth",
#     "whatever",
#     "hospital",
#     "pattern",
#     "smile",
#     "probably",
#     "at",
#     "evening",
#     "current",
#     "local",
#     "want",
#     "foreign",
#     "catch",
#     "option",
#     "meeting",
#     "course",
#     "collection",
#     "street",
#     "make",
#     "economic",
#     "fly",
#     "return",
#     "experience",
#     "east",
#     "position",
#     "foot",
#     "one",
#     "mean",
#     "break",
#     "me",
#     "truth",
#     "management",
#     "want",
#     "option",
#     "economic",
#     "response",
#     "attorney",
#     "table",
#     "push",
#     "travel",
#     "water",
#     "help",
# ]

# encode_words = [cipher.encode(word) for word in words]
# print(encode_words)

# decode_words = [cipher.decode(word) for word in encode_words]
# print(decode_words)

# # TEST_4:
# cipher = CaesarCipher(15)

# words = ['EvEr', 'WoUlD', 'CeRtAiN', 'WhIcH', 'WiTh', 'ThErE', 'EnViRoNmEnTaL', 'StRuCtUrE', 'NeWs', 'ThRoW', 'NoTe',
#          'If', 'WiN', 'ShOuLdEr', 'NeEd', 'WhErE', 'MeThOd', 'FiRsT', 'CiViL', 'BaSe']

# encode_words = [cipher.encode(word) for word in words]
# print(encode_words)

# decode_words = [cipher.decode(word) for word in encode_words]
# print(decode_words)

# # TEST_5:
# cipher = CaesarCipher(15)

# words = ['civil😀', 'so😁', 'region☺', 'beat☺', 'artist😍', 'choice🙃', 'include🤭', 'degree😝', 'push🤪', 'side😏', 'size🤥',
#          'policy🤨', '🤨🤥😏🤪😝🤭🙃😍☺😁😀']

# encode_words = [cipher.encode(word) for word in words]
# print(encode_words)

# decode_words = [cipher.decode(word) for word in encode_words]
# print(decode_words)

# TEST_6:
cipher = CaesarCipher(1)
print(cipher.encode("ZzzZzz"))
print(cipher.decode("AaaAaa"))
