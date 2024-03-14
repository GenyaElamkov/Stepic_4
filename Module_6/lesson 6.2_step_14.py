class OrderedSet:
    def __init__(self, iterable: set=()) -> None:
        self.iterable = iterable

    def add(self, value):
        set(self.iterable).add(value)

    def discard(self, value):
        set(self.iterable).discard(value)

    def __len__(self):
        return len(set(self.iterable))
    

    def __iter__(self):
        yield from set(self.iterable)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return self.iterable == __value.iterable
        
        if isinstance(__value, set):
            return self.iterable == __value
        return NotImplemented
    
    def __ne__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return self.iterable != __value.iterable
        
        if isinstance(__value, set):
            return self.iterable != __value
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.iterable)
    
# INPUT DATA:

# TEST_1:
orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))

# TEST_2:
orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print('python' in orderedset)
print('C++' in orderedset)

# TEST_3:
orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)

# TEST_4:
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
print(OrderedSet(['green', 'red', 'blue']) == 100)

# TEST_5:
data = ['Ada Lovelace'] * 1000
orderedset = OrderedSet(data)

print(len(orderedset))

# TEST_6:
orderedset = OrderedSet([1, 2, 3, 4])
not_supported = [120, {1: 'one'}, True, 'pi = 3', 17.9]

for item in not_supported:
    print(item != orderedset)

# TEST_7:
orderedset = OrderedSet([1, 2, 3, 4])
print(orderedset.__eq__(1))
print(orderedset.__ne__(1.1))