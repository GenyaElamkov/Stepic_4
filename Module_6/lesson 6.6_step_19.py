from contextlib import contextmanager


@contextmanager
def safe_write(filename: str):
    tmp_filename = "tmp_" + filename
    buffer = open(tmp_filename, "w")
    try:
        yield buffer
        buffer.close()
        with open(tmp_filename, "r") as file_1, open(filename, "w") as file_2:
            for line in file_1:
                file_2.write(line)

    except Exception as exp:
        print(f"Во время записи в файл было возбуждено исключение {type(exp).__name__}")


with safe_write("under_tale.txt") as file:
    file.write("Тень от руин нависает над вами, наполняя вас решительностью\n")

with safe_write("under_tale.txt") as file:
    print("Под весёлый шорох листвы вы наполняетесь решительностью", file=file)
    raise ValueError

with open("under_tale.txt") as file:
    print(file.read())
