class ReversedSequence:
    def __init__(self, sequence) -> None:
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)
    
    def __getitem__(self, key):
        return self.sequence[::-1][key]

    def __iter__(self):
        return iter(self.sequence[::-1])

    def __next__(self):
        return next(self.sequence)
    

# INPUT DATA:

print("TEST_1:")
reversed_list = ReversedSequence([1, 2, 3, 4, 5])

print(reversed_list[0])
print(reversed_list[1])
print(reversed_list[2])

print("TEST_2:")
numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)

print(reversed_numbers[0])
numbers.append(6)
print(reversed_numbers[0])

print("TEST_3:")
numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))

print("TEST_4:")
reversed_numbers = ReversedSequence((1, 2, 3, 4, 5))

for num in reversed_numbers:
    print(num)

print("TEST_5:")
reversed_chars = ReversedSequence('abcde')

for char in reversed_chars:
    print(char)

print("TEST_6:")
reversed_chars = ReversedSequence('abcdefghijklmnopqrstuvwxyz')

print(reversed_chars[0], reversed_chars[7], reversed_chars[11], reversed_chars[25])

print("TEST_7:")
reversed_list = ReversedSequence(['Gvido', 'Elon', 'Gates', 'Jobs', 'Zuckerberg'])

print(*reversed(reversed_list))