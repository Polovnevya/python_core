# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import random


def create_user_file(filename):
    """ Принимает текстовый параметр в качестве имени файлы который необходимо создать,
     далее программа заполняет файл случайными числами и закрывает файл

    :param filename: имя файла который необходимо создать и заполнить случайными числами
    :return: возвращает имя файла при успехе, иначе IOError
    """
    try:
        with open(filename, "w", encoding="utf-8") as f_user_obj:
            for line in range(1, 20):
                f_user_obj.write(str(round(random(), 3)))
                f_user_obj.write(" ")
            return filename
    except IOError:
        return IOError


def read_user_file(filename):
    """Открывает файл читает все строки за раз
    :param filename: Принимает имя файла вместе с расширением
    :return: возаращает список прочитаных строк, при неудаче возвращает ошибку IOError
    """
    try:
        with open(filename, "r", encoding="utf-8") as f_user_obj:
            return f_user_obj.readline().split()
    except IOError:
        return IOError


user_file_name = "text_5.txt"

result = read_user_file(create_user_file(user_file_name))
user_sum = 0
for el in result:
    user_sum += float(el)

print(f"Список числе сгенерированный и записанный в файл {user_file_name}")
print(' '.join(result))
print(f"Сумма всех чисел списка равна {user_sum}")
