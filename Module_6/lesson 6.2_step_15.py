class Closer:
    def __init__(self, obj) -> None:
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, *args, **kwargs)-> None:
        try:
            self.closed()
        except AttributeError:
            print("Незакрываемый объект")

    def closed(self)-> None:
        self.obj.close()


output = open("output.txt", "w", encoding="utf-8")

with Closer(output) as file:
    print(file.closed)

print(file.closed)

with Closer(5) as i:
    i += 1

print(i)
