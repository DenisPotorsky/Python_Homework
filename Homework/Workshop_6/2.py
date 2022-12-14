"""
Напишите программу, которая найдёт
произведение пар чисел списка.
Парой считаем первый и последний элемент,
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

# Старое решение

# lst = list(map(int, input('Создайте список: ').split()))
#
# temp = []
# length = len(lst) // 2
# if len(lst) % 2 > 0:
#     length += 1
# for i in range(length):
#     temp.append(lst[i] * lst[len(lst) - 1 - i])
# print(f'Произведение пар чисел списка: {temp}')

# Новое решение

lst = list(map(int, input('Создайте список: ').split()))

length = len(lst) // 2
if len(lst) % 2 > 0:
    length += 1
temp = [(lst[i] * lst[len(lst) - 1 - i]) for i in range(length)]
print(f'Произведение пар чисел списка: {temp}')
