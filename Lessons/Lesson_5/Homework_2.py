# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


def read_user_file(filename):
    """Открывает файл, читает его построчно, добавляет строки в список file_lines

    :param filename: Принимает имя файла вместе с расширением
    :return: возаращает список прочитаных строк file_lines, при неудаче возвращает ошибку IOError
    """
    file_lines = []
    try:
        with open(filename, "r", encoding="utf-8") as f_user_obj:
            for line in f_user_obj:
                file_lines.append(line.split())
            return file_lines
    except IOError:
        return IOError


print("Программа производит подсчет строк в файле и подсчет количества слов в каждой строке")
user_filename = "text_2.txt"
result = read_user_file(user_filename)
if result == IOError:
    print("Ошибка доступа к файлу {user_filename}.txt")
else:
    print(f"Количество строк в файле {len(result)}")
    for string in result:
        print(f"Количество слов в строке '{' '.join(string)}' насчитывается {len(string)}")
