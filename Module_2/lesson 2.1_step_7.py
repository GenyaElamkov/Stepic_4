"""
Покемоны
Артур владеет небольшой коллекцией карточек с покемонами, среди которых встречаются дубликаты. Он хочет оставить по одной карточке каждого типа, а остальные продать.

Напишите программу, которая определяет, сколько дубликатов из своей коллекции Артур может продать.

Формат входных данных
На вход программе подается произвольное количество строк, которые представляют коллекцию карточек с покемонами. В каждой строке указывается имя покемона с карточки.

Формат выходных данных
Программа должна вывести единственное число — количество карточек, которые из данной коллекции можно продать, чтобы оставить по одной карточке каждого типа.

Примечание 1. Рассмотрим первый тест. Чтобы оставить по одной карточке каждого типа, достаточно продать две карточки Pichu и одну карточку Tyrogue.

https://stepik.org/lesson/794484/step/7?unit=797232
"""

import sys

names = [name for name in sys.stdin.read().splitlines()]
print(len(names) - len(set(names)))