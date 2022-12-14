import import_export as imex
import logger as lg
import adding_an_entry

print('1. Показать все записи.')
print('2. Добавить новую запись.')
print('3. Импорт')
print('4. Экспорт')
print('5. Выход из меню')


def menu():
    while True:
        n = int(input('Выберите пункт меню: '))
        if n == 1:
            adding_an_entry.show_data()

        elif n == 2:
            lg.actions('User has selected command 2')
            name = input('Введите имя: ')
            lg.actions(f'User has entered name; {name}')
            surname = input('Введите фамилию: ')
            lg.actions(f'User has entered surname; {surname}')
            phone = input('Введите телефон: ')
            lg.actions(f'User has entered phone; {phone}')
            mail = input('Введите электронную почту: ')
            lg.actions(f'User has entered mail; {mail}')
            description = input('Введите примечание: ')
            lg.actions(f'User has entered description; {description}')
            adding_an_entry.new_entry(name, surname, phone, mail, description)
        elif n == 3:
            imex.import_entry()

        elif n == 4:
            ext = int(input('Выберите расширение: \n 1) .txt \n 2) .scv \n 3) .json \n 4) .html \n 5) .yml\n '))
            if ext == 1:
                imex.export_entry('txt')
            elif ext == 2:
                imex.export_entry('scv')
            elif ext == 3:
                imex.export_entry('json')
            elif ext == 4:
                imex.export_entry('html')
            elif ext == 5:
                imex.export_entry('yml')
        elif n == 5:
            break
