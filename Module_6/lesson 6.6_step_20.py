from contextlib import contextmanager


@contextmanager
def safe_open(filename: str, mode: str = "r"):
    try:
        file = open(filename, mode=mode)
        yield file, None
        file.close()
    except Exception as exp:
        yield None, exp


with open("Ellies_jokes.txt", "w") as file:
    file.write("Знаешь, кто не прав? Лев\n")
    file.write("Что треугольник сказал кругу? Катись отсюда")

with safe_open("Ellies_jokes.txt") as file:
    file, error = file
    print(error)
    print(file.read())
