'''
Задайте список из вещественных чисел.
Напишите программу, которая найдёт
разницу между максимальным и минимальным
значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

lst = list(map(float, input('Задайте список: ').split()))
maximum = 0
minimum = 0
result = 0
temp = []
for i in range(len(lst)):
    temp.append(lst[i] % 1)
    maximum = max(temp)
    minimum = min(temp)
result = maximum - minimum
print('Разница между максимальным и минимальным значением дробной части элементов: ', float('%.3f' % result))
