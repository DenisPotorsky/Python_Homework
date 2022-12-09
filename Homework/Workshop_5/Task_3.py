from random import randint

field = [i for i in range(1, 10)]


def print_field(f):
    for i in range(len(f)):
        if i % 3 == 0:
            print()
        print(f[i], end='' + '  |  ')
    print()


def your_turn(f):
    print('Ваш ход! ')
    cell = int(input('Выберите  ячейку: '))
    print('Ставим крестик :)')
    index = f.index(cell)
    f[index] = 'X'
    print_field(f)
    return f


def computer_turn(f):
    print('Мой ход!')
    print('Выбираю ячейку...')
    while True:
        cell = randint(0, 8)
        if f[cell] == 'X' or f[cell] == 'O':
            cell = randint(0, 8)
        else:
            f[cell] = 'O'
            break
    print_field(f)
    return f


def check_field(f):
    win_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
    for line in win_lines:
        if (f[line[0]] == 'X' and f[line[1]] == 'X' and f[line[2]] == 'X') or \
                (f[line[0]] == 'O' and f[line[1]] == 'O' and f[line[2]] == 'O'):
            return False
        else:
            return True


while True:
    computer_turn(field)
    if not check_field(field):
        print('Победил комп!')
        break
    your_turn(field)
    if not check_field(field):
        print('Вы победили!')
        break
    str_field = ''.join(str(field))
    if str_field.isalpha():
        print('Все ячейки закончились :( \n Ничья!')
        break
