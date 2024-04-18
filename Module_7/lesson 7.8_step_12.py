class Queue:
    def __init__(self, pairs=[]) -> None:
        self.pairs = pairs

    def add(self, n):
        pass

    def pop(self):
        pass

    def __repr__(self) -> str:
        pass

    def __len__(self):
        return len(self.pairs)
    

queue = Queue()

queue.add(('one', 1))
queue.add(('two', 2))
print(queue)