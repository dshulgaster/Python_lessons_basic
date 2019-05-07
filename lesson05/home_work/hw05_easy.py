import os
import shutil as sh

# отдельно выделенные функции для их последующего импорта
def make_dir_1__9():
    '''
    make_dir_1__9: функция создания директорий dir_1 - dir_9
    '''

    path = os.getcwd()
    for i in range(1, 10):
        path_i = os.path.join(path, 'dir_' + str(i))

        try:
            os.mkdir(path_i)
            print(f"Создана папка dir_{i} по пути: {path_i}")
        except FileExistsError:
            print(f"Невозможно создать папку по данному пути: {path_i}")

def del_dir_1__9():
    '''
    del_dir_1__9: функция удаления директорий dir_1 - dir_9
    '''

    path = os.getcwd()
    for i in range(1, 10):
        path_i = os.path.join(path, 'dir_' + str(i))

        try:
            os.rmdir(path_i)
            print(f"Удалена папка dir_{i} по пути: {path_i}")
        except FileNotFoundError:
            print(f"Невозможно удалить папку по данному пути: {path_i}")

def show_dir():
    '''
    show_dir: функция вывода папок в текущей директории
    '''
    currentPath = os.getcwd()
    # print("\nЧетвертый вариант (os.walk, но одной строкой):")
    print(next(os.walk(currentPath))[1])

    # print("\nПервый вариант:")
    # for i in os.listdir(currentPath):  # вариант 1
    #     dir_path = os.path.join(currentPath, i)
    #     if os.path.isdir(dir_path):
    #         print(i)
    #         # print(dir_path)
    #
    # print("\nВторой вариант (одной строкой):")
    # print([i for i in os.listdir(currentPath) if os.path.isdir(os.path.join(currentPath, i))]) # вариант 2
    #
    # print("\nТретий вариант (os.walk):")
    # for dirs in os.walk(currentPath): # вариант 3 - выводит и текущую папку, подумать, как доработать
    #     print(dirs[1])
    #     break

def copy_file():
    '''
    copy_file: функция копирования копии текущего файла
    '''

    # nameFile = os.path.realpath(__file__)
    # newFile = nameFile + '_copy'
    newFile = 'hw05_easy_copy.py'
    if os.path.isfile(newFile) != True:
        try:
            sh.copyfile(__file__, newFile)
            print(f"Скопирован текущий файл")
        except IOError:
            print(f"Невозможно cкопировать файл")
    else:
        print(f"Такой файл уже существует")

# функция для заданий hw05_normal
def change_dir():
    '''
    Запрашиваем у пользователя наименование папки, в которую
    необходимо перейти и осуществляем переход
    :return:
    '''
    newDir = input('Введите наименование папки для перехода в нее: ')
    dirPath = os.path.join(os.getcwd(), newDir)
    if os.path.exists(dirPath):
        os.chdir(dirPath)
        print(f"Переход в папку '{newDir}' осуществлен")
    else:
        print(f"Переход в папку '{newDir}' невозможен")

if __name__ == '__main__':
    # Задача-1:
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.

    print("Задача 1. Создать директории dir_1 - dir_9 в текущей папке.\n", '-' * 59, sep='')
    make_dir_1__9()
    # del_dir_1__9()
    print()

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.
    print("Задача 2. Отобразить папки текущей директории.\n", '-' * 46, sep='')
    show_dir()
    print()

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    print("Задача 3. Сделать копию файла, из которого запущен данный скрипт.\n", '-' * 65, sep='')
    copy_file()
