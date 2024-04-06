import sys
from contextlib import contextmanager


@contextmanager
def reversed_print():
    standart_output = sys.stdout.write
    sys.stdout.write = lambda text: standart_output(text[::-1])
    yield
    sys.stdout.write = standart_output


print("Вывод вне блока with")

with reversed_print():
    print("Вывод внутри блока with")

print("Вывод вне блока with")
