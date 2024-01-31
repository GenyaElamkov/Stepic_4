"""
Pycon
Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая проходит в четвертый четверг месяца.

Напишите программу, которая определяет день проведения очередной встречи питонистов в Сан-Диего.

Формат входных данных
На вход программе подается два натуральных числа, представляющие год и месяц, каждое на отдельной строке.

Формат выходных данных
Программа должна определить день проведения встречи в Сан-Диего в указанных году и месяце и вывести результат в формате DD.MM.YYYY.


https://stepik.org/lesson/794484/step/11?unit=797232
"""


import calendar

year, month = int(input()), int(input())
# year, month = int('2012'), int('3')
thursday = four_thursday = 3
day = calendar.monthcalendar(year, month)
if day[0][thursday] == 0:
    day = day[four_thursday + 1][thursday]
else:
    day = day[four_thursday][thursday]

print(f"{day:02}.{month:02}.{year}")
