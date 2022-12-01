'''
Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
'''

length = int(input('Введите длину списка: '))

lst1 = [0, 1]
lst2 = [1, -1]
# length = int(input())
result = 0
for i in range(1, length):
    result = lst1[i] + lst1[i - 1]
    lst1.append(result)
for j in range(1, length - 1):
    result = -(lst2[j]) + lst2[j - 1]
    lst2.append(result)
lst2.reverse()
fibonacci = lst2 + lst1

print(fibonacci)
