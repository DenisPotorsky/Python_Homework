'''
Напишите программу, которая принимает на вход число N
и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
Запрещено использовать функцию factorial из библиотеки math
'''

n = int(input('Enter the number: '))

result = 1

lts = []
for i in range(1, n + 1):
    result = result * i
    lts.append(result)
print(lts)
