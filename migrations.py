import os
import chardet

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def all_list():
    migrations_dir = os.path.join(current_dir, migrations)
    file_list = os.listdir(path=migrations_dir)
    return file_list


def sql_list(all_list):
    sql_file_list = list()
    for i in all_list:
        if i.endswith('.sql'):
            sql_file_list.append(i)
    return sql_file_list


def decode_files(file_name):
    with open(os.path.join(current_dir, migrations, file_name), 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        data = data.decode(result['encoding'])
        data = data.lower()
    return data


def search_string(sql_list):
    file_list = sql_list
    while True:
        search = input('Введите строку: ')
        search = search.lower()
        containing_files = list()
        for file_name in file_list:
            if search in decode_files(file_name):
                containing_files.append(file_name)
                print(file_name)
        print('Всего: {}'.format(len(containing_files)))
        file_list = containing_files


if __name__ == '__main__':
    search_string(sql_list(all_list()))

    pass