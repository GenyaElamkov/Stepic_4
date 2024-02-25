class Queue:
    def __init__(self, *args) -> None:
        self.__arr = [elem for elem in args]

    @property
    def arr(self) -> object:
        return self.__arr

    def add(self, *args) -> None:
        self.__arr.extend(args)

    def pop(self) -> int | None:
        if not self.__arr:
            return None
        return self.__arr.pop(0)

    def __str__(self) -> str:
        return " -> ".join(map(str, self.arr))

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return self.arr == __value.arr
        return NotImplemented

    def __ne__(self, __value: object) -> bool:
        if isinstance(__value, __class__):
            return self.arr != __value.arr
        return NotImplemented

    def __add__(self, other) -> object:
        if isinstance(other, __class__):
            new_inctanse = __class__(*self.arr)
            new_inctanse.add(other)
            return new_inctanse
        return NotImplemented

    def __iadd__(self, other: object):
        if isinstance(other, __class__):
            self.add(*other.arr)
            return self
        return NotImplemented

    def __rshift__(self, n: int):
        if not isinstance(n, int):
            return NotImplemented

        if n >= len(self.arr):
            return ""
        return __class__(*self.arr[n:])


queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)

queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)

queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

print(queue1 + queue2)


queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

queue1 += queue2

print(queue1)

queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)


queue = Queue(1, 2, 3, 4, 5)
id1 = id(queue)
print(queue)

queue += Queue(6, 7, 8, 9, 10)
id2 = id(queue)
print(queue)
print(id1 == id2)

queue = queue + Queue(11, 12, 13, 14, 15)
id3 = id(queue)

print(queue)
print(id1 == id3)

queue = Queue(*"beegeek")
for i in range(9):
    print(f"Queue >> {i} =", queue >> i)

# TEST_8:
queue = Queue(1)
item = queue.pop()
print(item)
print(queue.pop())

# TEST_9:
q1 = Queue(1, 2)
q2 = Queue(1, 2)

print(q1 == q2)
print(q1 != q2)

# TEST_10:
queue = Queue(1, 2, 3)
print(queue.__add__([]))
print(queue.__iadd__("bee"))
print(queue.__rshift__("geek"))
