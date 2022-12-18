import teacher
#import student
import autorization as au
import logger as lg

print('Добро пожаловать! Вас приветствует информационная система "Школик"')


def Menu():

    flag = True

    while flag:
        login = input('Введите логин:\n')
        lg.Log(f'User has entered login - {login}')
        password = input('Введите пароль:\n')
        lg.Log(f'User has entered password - {password}')
        
        status = au.control(login, password)

        if status == 1:
                print('Вы зашли как преподаватель. Выберите необходимое действие:\n'
                '1 - Написать ДЗ\n'
                '2 - Выставить оценки\n'
                '3 - Запрос админу\n'
                '4 - Выход\n')
                command = int(input('Выберите команду: '))
                lg.Log(f'User has selected command - {command}')
                teacher.enter(command)
        
        if status == 2:
                print('Вы зашли как ученик. Выберите необходимое действие:\n'
                '1 - Просмотр оценок\n'
                '2 - Просмотр ДЗ\n'
                '3 - Запрос админу\n'
                '4 - Выход\n')
                command = int(input('Выберите команду: '))
                lg.Log(f'User has selected command - {command}')
                student.read(command)


        if command == 5:
            lg.Log('User has selected command 5')
            flag = False


                    
            
