# для запуска приложений и передачи им аргументов
# для выполнения дочерней программы - класс Popen
import subprocess
# для управления директориями и файлами
import os
# для копирования, перемещения и удаление файлов и папок
import shutil
# для определения типа операционной системы
from sys import platform


# функция перехода в другой каталог
def SwitchingDirectory(current_directory, separator):
    direct = input('Введите назвние каталога: ')

    # обновление полного названия каталога
    directory = (current_directory + separator + direct)

    # возвращение списка с именами файлов и директорий в каталоге directory
    files = os.listdir(directory)
    for i in files:
        print(i)

    # изменение текущего рабочего каталога
    os.chdir(current_directory + separator + direct)

    # функция возвращает измененное полное название каталога
    return directory


# функция перехода на папку выше
def UpperDirectory(current_directory, separator):
    # делаем массив из названий папок
    directory_array = current_directory.split(separator)
    print(directory_array[-1])

    # делаем массив для удаления из полного названия лишней папки
    directory = current_directory.split(separator + directory_array[-1])
    print(directory[0])

    # функция выводит новое полное название каталога
    return directory[0]


# функция удаления файла в каталоге
def DeleteFile(current_directory, separator):
    file_path = input('Введите путь к файлу для удаления: ')

    # удаляем файл
    os.remove(current_directory + separator + file_path, dir_fd=None)
    print('Готово! Файл ', file_path, ' удален из директории: ', current_directory)



# функция удаления каталога
def DeleteDirectory(current_directory, separator):
    directory_path = input('Введите путь к каталогу для удаления: ')

    # удаление каталога
    os.rmdir(current_directory + separator + directory_path)
    print('Готово! Каталог ', directory_path, ' удален из: ', current_directory)


# функция создания нового файла
def NewFile(current_directory):
    file_name = input('Введите имя и расширение файла: ')

    # открытие файла
    # параметр w означает, что файл открыт для записи (перед записью файл будет очищен)
    open(file_name, "w")
    print('Файл создан в директории: ', current_directory, ' с именем ', file_name)


# функция создания новой папки
def NewFolder(current_directory):
    folder_name = input('Введите название паки чтобы создать ее в директории: ')

    # создание папки
    os.mkdir(folder_name)
    print('Готово! Папка создана с именем - ', folder_name, ' в директории: ', current_directory)


# функция просмотра содержимого файла
def ReadFile(current_directory, separator):
    in_file = input('Введите путь к файлу: ')

    # открываем файл
    my_file = open(current_directory + separator + in_file)

    # аписываем содержимое в переменную my_string
    my_string = my_file.read()
    print(my_string)

    # закрываем файл
    my_file.close()

    print('Прочитан файл - ', in_file)


# функция добавления содержимого в файл
def AddContentFile(current_directory, separator):
    in_file = input('Введите путь к файлу: ')

    # открываем файл
    # параметр a означает, что файл открыт для добавления в конец
    my_file = open(current_directory + separator + in_file, "a")
    writing = input('Введите текст: \n')
    my_file.write(writing)
    my_file.close()

    print('Запись сдедлана в файл - ', in_file)


# функция копирования файла в другой каталог
def CopyFile(current_directory, separator):
    path1 = input('Введите путь файла, который нужно скопировать: \n')
    path2 = input('Введите путь, куда нужно скопировать: \n')

    # копируем файл
    shutil.copy2(current_directory + separator + path1, current_directory + separator + path2)

    print('Файл скопирован в ', current_directory + separator + path2)


# функция перемещения файла в другой каталог
def MoveFile(current_directory, separator):
    path1 = input('Введите путь файла, который нужно переместить: \n')
    path2 = input('Введите путь, куда нужно переместить: \n')

    # перемещаем файл в указанный каталог
    shutil.move(current_directory + separator + path1, current_directory + separator + path2)

    print('Файл перемещен в ', current_directory + separator + path2)


# функция переименования файла
def RenameFile(current_directory, separator):
    path1 = input('Введите путь файла, который нужно переименовать: \n')
    path2 = input('Введите новое имя: \n')

    # переименовываем файл и сразу меняем полный путь
    os.rename(current_directory + separator + path1, current_directory + separator + path2)
    print('Файл переименован. Новый путь: ', current_directory + separator + path2)


# функция открытия файла
def OpenFile():
    open_file = input('Введите название файла: ')

    # для выполнения дочерней программы - класс Popen
    subprocess.Popen(open_file, shell=True)


# основной класс
def __main__():

    # автоматическое определение ос и вывод соответствующего сообщения
    if platform == "linux" or platform == "linux2":
        separator = '/'
        current_directory = input('\nВведите полное название католога в виде /home \n')
    elif platform == "win32" or platform == "win64":
        separator = '\\'
        current_directory = input('\nВведите полное название католога в виде C:\ \n')

    # для цикла while
    c = ''

    # домашнй директории присваиваем значение текущей (дальше для проверки)
    home_directory = current_directory

    # программа работает, пока пользователь не напишет stop
    while c != 'stop':

        # возвращение списка с именами файлов и директорий в каталоге directory
        files = os.listdir(current_directory)

        print('\nТекущий каталог: ', current_directory)
        print('Домашний каталог: ', home_directory)

        users_input = input('\nВведите комманду (help - список команд): ')
        if users_input == 'help':
            print("\n1. Перейти в другой каталог либо в католог в этой папке"
                  "\n2. Перейти на папку выше "
                  "\n3. Отобразить содержимое текущей папки "
                  "\n4. Создать файл "
                  "\n5. Создать папку "
                  "\n6. Удалить файл в катологе "
                  "\n7. Удалить каталог "
                  "\n8. Посмотреть содержимое файла "
                  "\n9. Сделать запись в файл "
                  "\n10. Скопировать файл в другой каталог "
                  "\n11. Переместить файл в другой каталог "
                  "\n12. Переименовать файл "
                  "\n13. Открыть файл"
                  "\nstop для остановки программы\n")

        elif users_input == '1':
            current_directory = SwitchingDirectory(current_directory, separator)

        elif users_input == '2':
            if current_directory == home_directory:
                print('Невозможно подняться выше домашнего каталога!')
            else:
                current_directory = UpperDirectory(current_directory, separator)

        elif users_input == '3':
            for i in files:
                print(i)

        elif users_input == '4':
            NewFile(current_directory)

        elif users_input == '5':
            NewFolder(current_directory)

        elif users_input == '6':
            DeleteFile(current_directory, separator)

        elif users_input == '7':
            DeleteDirectory(current_directory, separator)

        elif users_input == '8':
            ReadFile(current_directory, separator)

        elif users_input == '9':
            AddContentFile(current_directory, separator)

        elif users_input == '10':
            CopyFile(current_directory, separator)

        elif users_input == '11':
            MoveFile(current_directory, separator)

        elif users_input == '12':
            RenameFile(current_directory, separator)

        elif users_input == '13':
            OpenFile()

        elif users_input == 'stop':
            print('Выхожу из программы!')

        else:
            print('Введена неверная команда\nОткатываемся\nВведите путь заново: ')


if __name__ == "__main__":
    __main__()
