'''
 Задайте список из N элементов,
 заполненных числами из промежутка [-N, N].
 Найдите произведение элементов на указанных позициях.
 Позиции вводятся с клавиатуры.
'''

import random

n = int(input('Введите количество элементов списка: '))

lst = []
for i in range(n):
    lst.append(random.randint(-n, n))
print(lst)

result = 1
index = 0
num_pos = int(input('Введите количество проверяемых позиций: '))
for i in range(num_pos):
    index = int(input(f'Введите номер {i + 1}-го элемента: '))
    result *= lst[index - 1]
print(f'Произведение элементов на указанных позициях: {result}')
