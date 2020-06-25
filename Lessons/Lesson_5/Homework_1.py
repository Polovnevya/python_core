# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


def write_2_file(user_filename, user_string):
    """Записть в файл реализована через print
    Если возникает ошибка доступа к файлу возвращает ошибку "IOError"

    :param user_filename: Имя файла для записи, по умолчанию к имени добавляет расширение .txt
    :param user_string: Строка которая будет записываться в файл
    :return: Возвращает ошибку при неудачном обращении к файлу
    """
    try:
        with open(f"{user_filename}.txt", "a+") as f_user_obj:
            print(user_string, file=f_user_obj)
    except IOError:
        return IOError


def write_2_file_v2(user_filename, user_string):
    """Записть в файл реализована через метод write()
    Если возникает ошибка доступа к файлу возвращает ошибку "IOError"

    :param user_filename: Имя файла для записи, по умолчанию к имени добавляет расширение .txt
    :param user_string: Строка которая будет записываться в файл
    :return: Возвращает ошибку при неудачном обращении к файлу
    """
    try:
        with open(f"{user_filename}_v2.txt", "a+") as f_user_obj:
            f_user_obj.write(f"{user_string}\n")
    except IOError:
        return IOError


print("Введите данные для записи в файл\n"
      "Для выхода из программы нажмите Enter при пустой строке")

filename = input("Введите имя файла ")
user_line = input("Введите строку ")
while user_line != "":
    result = write_2_file(filename, user_line)
    result_v2 = write_2_file_v2(filename, user_line)
    if result == IOError:
        print("Ошибка доступа к файлу {user_filename}.txt")
        break
    elif result_v2 == IOError:
        print("Ошибка доступа к файлу {user_filename}_v2.txt")
        break
    user_line = input("Введите строку ")
