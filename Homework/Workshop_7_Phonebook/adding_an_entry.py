def new_entry(name, surname, number, email, description):
    with open('data_file.txt', 'a') as data:
        data.write('\n {}; {}; {}; {}; {} \n'.format(name, surname, number, email, description))
        print()


def show_data():
    with open('data_file.txt', 'r') as data:
        lines = data.readlines()
        for line in lines:
            print(line)
