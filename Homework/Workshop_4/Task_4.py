"""
Задана натуральная степень k.
Сформировать случайным образом список
коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

from random import randint
import sys

degree = int(input('Задайте степень:  '))
if degree < 1:
    sys.exit('Введена неверная степень')


def generate_list(k):
    lst = [randint(0, 101) for _ in range(k + 1)]
    return lst


def create_str(factors):
    polynom = ''
    for i in range(len(factors)):
        if i != len(factors) - 1 and factors[i] != 0 and i != len(factors) - 2:
            polynom += f'{factors[i]} x**{len(factors) - i - 1}'
            if factors[i + 1] != 0:
                polynom += ' + '
        elif i == len(factors) - 2 and factors[i] != 0:
            polynom += f'{factors[i]} * x'
            if factors[i + 1] != 0:
                polynom += ' + '
        elif i == len(factors) - 1 and factors[i] != 0:
            polynom += f'{factors[i]} = 0'
        elif i == len(factors) - 1 and factors[i] == 0:
            polynom += ' = 0'
    return polynom


st = create_str(generate_list(degree))
st2 = create_str(generate_list(degree))

with open('Task_4.txt', 'w') as data:
    data.write(st)

with open('Task_5.txt', 'w') as data1:
    data1.write(st2)
