"""
Координаты
Географические координаты представляют собой пару чисел 
Напишите программу, которая принимает произвольное количество строк и определяет, какие из них представляют собой корректные географические координаты.

Формат входных данных
На вход программе подается произвольное количество строк, каждая из которых представляет собой пару чисел в следующем формате:

(<координата x>, <координата y>)
Формат выходных данных
Программа должна для каждой строки вывести True, если она представляет собой корректные географические координаты, или False в противном случае.

https://stepik.org/lesson/794484/step/9?unit=797232
"""

import sys

for line in sys.stdin.read().splitlines():
    line = line.replace('(', '').replace(')', '').split(',')
    x, y = map(float, line)
    if -90 <= x <= 90 and -180 <= y <= 180:
        print(True)
    else:
        print(False)