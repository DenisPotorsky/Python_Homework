"""
Даны два файла, в каждом из которых
находится запись многочлена.
Задача - сформировать файл,
содержащий сумму многочленов.
"""

from Task_4 import create_str

with open('Task_4.txt', 'r') as file:
    first = file.readline()
with open('Task_5.txt', 'r') as file:
    second = file.readline()


def make_list(values):
    lst = []
    nums = values.split()
    index = 0
    for i in nums:
        if i.isnumeric():
            lst.append(int(i))
            index += 1
    return lst


first_list = make_list(first)
second_list = make_list(second)

result = []
for i in range(len(first_list) - 1):
    result.append(first_list[i] + second_list[i])

third_poly = create_str(result)
with open('Task_5.1.txt', 'w') as file:
    file.write(third_poly)
