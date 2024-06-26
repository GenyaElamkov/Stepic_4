class Counter:
    def __init__(self, start: int = 0) -> None:
        self.value = start

    def inc(self, n: int = 1):
        self.value += n

    def dec(self, n: int = 1):
        self.value = max(self.value - n, 0)


class NonDecCounter(Counter):
    def dec(self, n: int = 1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start: int = 0, limit: int = 10) -> None:
        Counter.__init__(self, start)
        self.limit = limit

    def inc(self, n: int = 1):
        self.value = min(self.value + n, self.limit)


# INPUT DATA:

# TEST_1:
print(issubclass(NonDecCounter, Counter))
print(issubclass(LimitedCounter, Counter))

# TEST_2:
counter = Counter()

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(3)
print(counter.value)
counter.dec(10)
print(counter.value)

# TEST_3:
counter = NonDecCounter(10)

print(counter.value)
counter.inc()
counter.inc(10)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(50)
print(counter.value)

# TEST_4:
counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)

# TEST_5:
counter = LimitedCounter(limit=20)

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)

# TEST_6:
counter = LimitedCounter(start=5, limit=30)

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(24)
print(counter.value)

# TEST_7:
digits = [
    55,
    40,
    110,
    183,
    78,
    181,
    172,
    158,
    146,
    35,
    60,
    180,
    102,
    170,
    62,
    46,
    181,
    68,
    103,
    124,
    130,
    127,
    161,
    107,
    199,
    100,
    74,
    120,
    132,
    65,
    167,
    28,
    45,
    158,
    53,
    122,
    86,
    29,
    199,
    129,
    97,
    71,
    113,
    54,
    134,
    45,
    76,
    157,
    25,
    60,
]

counter = Counter(10)

pos = True

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)

# TEST_8:
digits = [
    105,
    128,
    149,
    107,
    119,
    60,
    60,
    60,
    188,
    61,
    154,
    88,
    161,
    99,
    199,
    121,
    77,
    33,
    185,
    95,
    182,
    128,
    166,
    167,
    153,
    115,
    199,
    124,
    109,
    65,
    118,
    20,
    175,
    194,
    149,
    184,
    174,
    162,
    36,
    51,
    134,
    196,
    132,
    129,
    95,
    199,
    150,
    55,
    123,
    100,
]

counter = NonDecCounter(10)

pos = True

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)

# TEST_9:
digits = [
    46,
    158,
    79,
    100,
    161,
    100,
    30,
    27,
    132,
    79,
    152,
    114,
    97,
    171,
    71,
    35,
    186,
    157,
    149,
    144,
    156,
    41,
    172,
    122,
    131,
    141,
    69,
    113,
    86,
    46,
    104,
    147,
    42,
    60,
    31,
    32,
    190,
    107,
    110,
    103,
    77,
    135,
    35,
    33,
    104,
    191,
    94,
    55,
    50,
    156,
]

counter = LimitedCounter(start=10, limit=2000)

pos = True

for digit in digits:
    if pos:
        counter.inc(digit)
    else:
        counter.dec(digit)
    pos = not pos

print(counter.value)
