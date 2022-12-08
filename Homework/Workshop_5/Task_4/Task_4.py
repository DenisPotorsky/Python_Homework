"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff
"""

s = 'aaaasssdddwwwwwwwwwwwweeeffffff'

with open('decoded.txt', 'w') as data:
    text = data.write(s)


def encoded(s):
    count = 1
    new_data = ''
    i = 0
    while i < len(s):
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        new_data += str(count) + s[i]
        count = 1
        i += 1
    return new_data


res_e = encoded(s)

with open('encoded.txt', 'w') as data:
    text1 = data.write(res_e)


def decoded(z):
    result_dec = ''
    num = ''
    for i in range(len(z)):
        if z[i].isdigit():
            num += z[i]
        else:
            result_dec += z[i] * int(num)
            num = ''
    return result_dec


res_d = decoded(res_e)
