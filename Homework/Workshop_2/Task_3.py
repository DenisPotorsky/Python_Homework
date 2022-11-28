'''
 Задайте список из n чисел последовательности
 (1 + 1 / n)**n и выведите на экран их сумму.
Пример:
- Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52] -> 14.072
(Округлять не обязательно)
'''

n = int(input('Введите число: '))

lst = []
result = 0
for i in range(1, n + 1):
    result = result + (1 + 1 / i) ** i
    lst.append((1 + 1 / i) ** i)
print(f'Список: {lst}')
print(f'Сумма: {result}')
