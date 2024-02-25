class Filter:
    def __init__(self, predicate) -> None:
        self.predicate = predicate

    def __call__(self, iterable):
        return list(filter(self.predicate, iterable))


leave_even = Filter(lambda x: x % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6]

print(leave_even(numbers))

more_than_five = Filter(lambda x: x > 5)
numbers = [13, 1, 4, 10, 10, 7]

print(more_than_five(numbers))

non_empty = Filter(None)

sequence = ([], False, 1, (), "Linus Torvalds", {5, 6, 7}, True, {}, set(), "")
print(non_empty(sequence))
