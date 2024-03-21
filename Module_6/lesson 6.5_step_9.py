import sys


class UpperPrint:
    def __enter__(self):
        self.old_stdout = sys.stdout.write
        sys.stdout.write = lambda x: self.old_stdout(x.upper())

    def __exit__(self, *args, **kwargs):
        sys.stdout.write = self.old_stdout


print("Если жизнь одаривает вас лимонами — не делайте лимонад")
print("Заставьте жизнь забрать их обратно!")

with UpperPrint():
    print("Мне не нужны твои проклятые лимоны!")
    print("Что мне с ними делать?")

print("Требуйте встречи с менеджером, отвечающим за жизнь!")
