"""
Напишите программу, удаляющую из файла все слова, содержащие "абв".
"""
# Первоначальное решение, оставил как есть.

text = input('Введите текст: ')

with open('File.txt', 'w') as data:
    data.write(text)


def del_words(txt):
    txt = list(filter(lambda x: 'абв' not in x, txt.split()))
    return " ".join(txt)


text = del_words(text)
print(text)
