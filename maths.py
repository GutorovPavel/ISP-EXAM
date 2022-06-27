import re

OPERATORS = {
        '+': float.__add__,
        '-': float.__sub__,
        '*': float.__mul__,
        '/': float.__idiv__,
        '%': float.__mod__,
        '^': float.__pow__,
    }


def reversed_polish_notation(expr):
    """
    Возвращает результат вычисленного выражения записанного в виде обратной
    польской нотации
    expr = string
    """
    ops = OPERATORS.keys()
    stack = []

    for atom in re.split(r"\s+", expr):
        try:
            atom = float(atom)
            stack.append(atom)
        except ValueError:
            for oper in atom:
                if oper not in ops:
                    continue
                try:
                    oper2 = stack.pop()
                    oper1 = stack.pop()
                except IndexError:
                    raise Exception(u"Маловато операндов")

                try:
                    oper = OPERATORS[oper](oper1, oper2)
                except ZeroDivisionError:
                    raise Exception(u"Нельзя делить на 0")

                stack.append(oper)

    if len(stack) != 1:
        raise Exception(u"Многовато операндов")

    return stack.pop()


############# Баланс скобок ##############

"""  Если кортеж
t = (a, b, c)
s = str()

for i in t:
    s ++ i
"""

"""
string = input()
arr = []

for val in string:
    if val == '{' or val == '[' or val == '(':
        arr.append(val)

    if val == '}' or val == ']' or val == ')':
        if len(arr) == 0:
            raise ValueError(f'{string[:string.find(val)] > string[string.find(val):]}')
        delee = arr.pop(len(arr) - 1)
        if not chr(ord(val) - 2) == delee and not chr(ord(val) - 1) == delee:
            raise ValueError(f'{string[:string.find(val)]} > {string[string.find(val):]}')

if not len(arr) == 0:
    raise ValueError(f'{string} <')

"""

##########################################
