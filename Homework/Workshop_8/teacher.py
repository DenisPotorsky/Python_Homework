import logger as lg
import autorization as cont
import menu 


def Password(command, password):
    if command == 1:
        cnt = cont.Teacher(password)
    else:
        cnt = cont.Students(password)
    return cnt


def Enter_info(subcommand1, subcommand2, subcommand3):
#     if subcommand1 == 1 and subcommand2 == 1 and subcommand3 == 1:
#         #with open('8S_HW\_5A_Russian_language_score.csv', 'a') as file:
#             #writer_score = csv.writer(file, delimiter=';')
#             # for row in writer_score:
    
    if subcommand1 == '1' and subcommand2 == '1' and subcommand3 == '2':
        message = input('Введите домашнее задание: ')
        with open('8S_HW\_5A_Russian_language_homework.csv', 'a', encoding='utf-8') as file:
            file.write(message)


