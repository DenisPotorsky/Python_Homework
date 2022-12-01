'''
Реализуйте алгоритм перемешивания списка.
Из библиотеки random использовать можно только randint.
'''
import random

lst = [1, 2, 3, 4, 5]
temp = 0
index = 0
for i in range(len(lst)):
    index = random.randint(0, len(lst) - 1)
    lst[i], lst[index] = lst[index], lst[i]

print(lst)
