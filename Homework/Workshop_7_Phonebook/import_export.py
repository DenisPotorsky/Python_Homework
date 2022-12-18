def import_entry():
    with open('123.txt', 'r') as import_file:
        data = import_file.readlines()
        with open('data_file.txt', 'a') as file:
            for line in data:
                file.write(line)
                print()


def export_entry(extension):
    with open('data_file.txt', 'r') as export_file:
        data = export_file.readlines()
        with open(f'temp_file.{extension}', 'w') as temp_file:
            temp_file.writelines(data)
