class ValueDict(dict):
    def key_of(self, value):
        for key, val in self.items():
            if val == value:
                return key

    def keys_of(self, value):
        return [k for k, v in self.items() if v == value]


# INPUT DATA:

# TEST_1:
valuedict = ValueDict({"apple": 1, "banana": 2, "orange": 2})

print(valuedict.key_of(2))
print(*valuedict.keys_of(2))

# TEST_2:
countries = {
    "Monaco": "Monaco",
    "Iceland": "Reykjavik",
    "Kenya": "Nairobi",
    "Kazakhstan": "Nur-Sultan",
    "Mali": "Bamako",
    "Colombia": "Bogota",
    "Finland": "Helsinki",
    "Costa Rica": "San Jose",
    "Cuba": "Havana",
    "France": "Paris",
    "Gabon": "Libreville",
    "Liberia": "Monrovia",
    "Angola": "Luanda",
    "India": "New Delhi",
    "Canada": "Ottawa",
    "Australia": "Canberra",
}

valuedict = ValueDict(countries)

print(valuedict.key_of("Moscow"))
print(*valuedict.keys_of("Washington"))

# TEST_3:
valuedict = ValueDict({})

print(valuedict.key_of(12))
print(*valuedict.keys_of(33))

# TEST_4:
data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


valuedict = ValueDict(data)

print(valuedict.key_of(21))
print(*valuedict.keys_of(17))

# TEST_5:
data = {
    0: 1,
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
    7: 1,
    8: 1,
    9: 1,
    10: 1,
    11: 1,
    12: 1,
    13: 1,
    14: 1,
    15: 1,
    16: 1,
    17: 1,
    18: 1,
    19: 1,
    20: 1,
    21: 1,
    22: 1,
    23: 1,
    24: 1,
    25: 1,
    26: 1,
    27: 1,
    28: 1,
    29: 1,
    30: 1,
    31: 1,
    32: 1,
    33: 1,
    34: 1,
    35: 1,
    36: 1,
    37: 1,
    38: 1,
    39: 1,
    40: 1,
    41: 1,
    42: 1,
    43: 1,
    44: 1,
    45: 1,
    46: 1,
    47: 1,
    48: 1,
    49: 1,
    50: 1,
    51: 1,
    52: 1,
    53: 1,
    54: 1,
    55: 1,
    56: 1,
    57: 1,
    58: 1,
    59: 1,
    60: 1,
    61: 1,
    62: 1,
    63: 1,
    64: 1,
    65: 1,
    66: 1,
    67: 1,
    68: 1,
    69: 1,
    70: 1,
    71: 1,
    72: 1,
    73: 1,
    74: 1,
    75: 1,
    76: 1,
    77: 1,
    78: 1,
    79: 1,
    80: 1,
    81: 1,
    82: 1,
    83: 1,
    84: 1,
    85: 1,
    86: 1,
    87: 1,
    88: 1,
    89: 1,
    90: 1,
    91: 1,
    92: 1,
    93: 1,
    94: 1,
    95: 1,
    96: 1,
    97: 1,
    98: 1,
    99: 1,
}

valuedict = ValueDict(data)

print(valuedict.key_of(1))
print(*valuedict.keys_of(1))
