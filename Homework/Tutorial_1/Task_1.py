'''
Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, 
является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
'''

day = int(input('Enter the number: '))

if day < 1 or day > 7:
    print('ERROR')
elif day == 6 or day == 7:
    print('yes')
else:
    print('no')
