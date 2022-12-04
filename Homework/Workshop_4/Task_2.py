"""
Задайте натуральное число N.
Напишите программу, которая составит
список простых множителей числа N.
"""


def list_creation(n):
    lst = []
    x = 2
    while x * x <= n:
        if n % x == 0:
            lst.append(x)
            n //= x
        else:
            x += 1
    if n > 1:
        lst.append(n)
    return lst


print(list_creation(int(input('Введите число: '))))
