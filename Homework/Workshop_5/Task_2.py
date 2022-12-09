from random import randint

candies = 2021
first_move = randint(0, 1)


def gamer_turn(count):
    print('Ваш ход! \n Сколько возьмем конфет??')
    while True:
        move = int(input())
        if move > 28:
            print('Перебор! Не больше 28 конфет! ')
        else:
            break
    return move


def computer_turn(count, turn):
    print('Ход компьютера')
    if turn == 1:
        move = count % 29
    else:
        move = randint(1, 28)
    print(f'Возьму {move} конфет')
    return move


while candies > 0:
    if first_move == 0:
        candies -= gamer_turn(candies)
        print(f'Осталось: {candies}')
        if candies == 0:
            print('you win')
            break
        candies -= computer_turn(candies, first_move)
        print(f'Осталось: {candies}')
        if candies == 0:
            print('comp win')
            break
    else:
        candies -= computer_turn(candies, first_move)
        print(f'Осталось: {candies}')
        if candies == 0:
            print('Комп победил!')
            break
        candies -= gamer_turn(candies)
        print(f'Осталось: {candies}')
        if candies == 0:
            print('Вы выиграли!')
            break


