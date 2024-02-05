class Todo:
    def __init__(self) -> None:
        self.things = []

    def add(self, name: str, priority: int) -> None:
        self.things.append((name, priority))

    def get_by_priority(self, n: int) -> list[str]:
        return [name[0] for name in filter(lambda x: x[1] == n, self.things)]

    def get_low_priority(self) -> list[str]:
        if not self.things:
            return []
        low = min(map(lambda x: x[1], self.things))
        return self.get_by_priority(low)

    def get_high_priority(self):
        if not self.things:
            return []
        high = max(map(lambda x: x[1], self.things))
        return self.get_by_priority(high)


todo = Todo()

todo.add("Ответить на вопросы", 5)
todo.add("Сделать картинки", 1)
todo.add("Доделать задачи", 4)
todo.add("Дописать конспект", 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))
