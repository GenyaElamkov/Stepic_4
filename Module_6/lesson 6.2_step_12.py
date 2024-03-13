from itertools import cycle

class CyclicList:
    def __init__(self, iterable) -> None:
        self.iterable = iterable

    def append(self, object):
        ...

    def pop(self, key):
        ...

    def __len__(self):
        return len(self.iterable)
    
    def __getitem__(self, key):
        return self.iterable[key]
    


cyclic_list = CyclicList([1, 2, 3])

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')