"""
Скобочная последовательность
Назовем скобочной последовательностью строку, состоящую из символов ( и ). Будем считать скобочную последовательность правильной, если:

для каждой открывающей скобки есть закрывающая скобка
скобки закрываются в правильном порядке, то есть в каждой паре из открывающей и закрывающей скобок открывающая находится левее
Напишите программу, которая определяет, является ли скобочная последовательность правильной.

Формат входных данных
На вход программе подается строка, представляющая собой скобочную последовательность.

Формат выходных данных
Программа должна вывести True, если введенная скобочная последовательность является правильной, или False в противном случае.

https://stepik.org/lesson/794484/step/5?unit=797232
"""

import re


def couple(text: str) -> bool:
    if text == "()" or not text:
        return True
    try:
        text = re.sub(r"\B\(\)\B", r"", text)
        return couple(text)
    except RecursionError:
        return False


t = "(())))(()((()))(()())((()"
print(couple(t))


# s = input()
# while re.search(r'\(\)', s):
#     s = re.sub(r'\(\)', '', s)

# print(not s)

brackets = input()
stack = []


def check_brackets(brackets: str) -> bool:
    stack = []
    for symbol in brackets:
        if symbol == "(":
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True


print(check_brackets(brackets))
