import os


def create_file(FILE_NAME):
    ROOT_PATH = os.getcwd()
    full_path = os.path.join(ROOT_PATH, FILE_NAME)
    return full_path


first_file = create_file('t.txt')
second_file = create_file('t1.txt')
third_file = create_file('t2.txt')


def create_file_name(FILE_NAME):
    FILE_NAME = os.path.basename(FILE_NAME)
    return FILE_NAME


first_file_name = create_file_name(first_file)
second_file_name = create_file_name(second_file)
third_file_name = create_file_name(third_file)


def find_len_of_file(FILE):
    with open(FILE, encoding='UTF-8') as file:
        len_of_file = len(file.readlines())
    return len_of_file


len_of_first_file = find_len_of_file(first_file)
len_of_second_file = find_len_of_file(second_file)
len_of_third_file = find_len_of_file(third_file)


def read_file(FILE):
    with open(FILE, encoding='UTF-8') as file:
        file_ = file.read()
    return file_


readed_first_file = read_file(first_file)
readed_second_file = read_file(second_file)
readed_third_file = read_file(third_file)

with open('new_file.txt', 'wt', encoding='UTF-8') as file:
    if len_of_third_file < len_of_second_file < len_of_first_file:
        file.write(f'{third_file_name}\n{len_of_third_file}\n{readed_third_file}\n'
                   f'{second_file_name}\n{len_of_second_file}\n{readed_second_file}\n'
                   f'{first_file_name}\n{len_of_first_file}\n{readed_first_file}')
    elif len_of_third_file < len_of_first_file < len_of_second_file:
        file.write(f'{third_file_name}\n{len_of_third_file}\n{readed_third_file}\n'
                   f'{first_file_name}\n{len_of_first_file}\n{readed_first_file}\n'
                   f'{second_file_name}\n{len_of_second_file}\n{readed_second_file}')
    elif len_of_second_file < len_of_third_file < len_of_first_file:
        file.write(f'{second_file_name}\n{len_of_second_file}\n{readed_second_file}\n'
                   f'{third_file_name}\n{len_of_third_file}\n{readed_third_file}\n'
                   f'{first_file_name}\n{len_of_first_file}\n{readed_first_file}')
    elif len_of_second_file < len_of_first_file < len_of_third_file:
        file.write(f'{second_file_name}\n{len_of_second_file}\n{readed_second_file}\n'
                   f'{first_file_name}\n{len_of_first_file}\n{readed_first_file}\n'
                   f'{third_file_name}\n{len_of_third_file}\n{readed_third_file}')
    elif len_of_first_file < len_of_third_file < len_of_second_file:
        file.write(f'{first_file_name}\n{len_of_first_file}\n{readed_first_file}\n'
                   f'{third_file_name}\n{len_of_third_file}\n{readed_third_file}\n'
                   f'{second_file_name}\n{len_of_second_file}\n{readed_second_file}')
    elif len_of_first_file < len_of_second_file < len_of_third_file:
        file.write(f'{first_file_name}\n{len_of_first_file}\n{readed_first_file}\n'
                   f'{second_file_name}\n{len_of_second_file}\n{readed_second_file}\n'
                   f'{third_file_name}\n{len_of_third_file}\n{readed_third_file}')




