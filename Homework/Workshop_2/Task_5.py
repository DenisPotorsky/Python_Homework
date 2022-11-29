'''
Реализуйте алгоритм перемешивания списка.
Из библиотеки random использовать можно только randint.
'''
import random

lst = [1, 2, 3, 4, 5]
temp = 0
index = 0
for i in range(0, 5):
    index = random.randint(0, 4)
    temp = lst[i]
    lst[i] = lst[index]
    lst[index] = temp

print(lst)
