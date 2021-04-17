import sys
from igra import game
from core import create_file, create_folder, get_list, delete_file, copy_file, safe_info, change_dir

safe_info('старт')
try:
    command = sys.argv[1]
except IndexError:
    print('Отсутствует команда. help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла или папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Необходимо ввести название (файла, папки) и название копии')
        else:
            copy_file(name, new_name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название директории')
        else:
            change_dir(name)
    elif command == 'game':
        game()
    elif command == 'help':
        print('list ---------- Список файлов и папок')
        print('create_file --- Создать файл')
        print('create_folder - Создать папку')
        print('delete -------- Удалить файл или папку')
        print('copy ---------- Копировать файл или папку')
        print('ch ------------ Сменить дерикторию')
        print('game ---------- Игра "Угадай число"')
safe_info('конец')
