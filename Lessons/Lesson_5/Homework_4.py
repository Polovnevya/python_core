# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


def read_user_file(user_filename):
    """Открывает файл читает построчно
    :param user_filename: Принимает имя файла вместе с расширением
    :return: возаращает список прочитаных строк file_lines, при неудаче возвращает ошибку IOError
    """
    file_lines = []
    try:
        with open(user_filename, "r", encoding="utf-8") as f_user_obj:
            for line in f_user_obj:
                file_lines.append(line.replace("\n", "").split("-"))
            return file_lines
    except IOError:
        return IOError


filename = "text_4.txt"
result = read_user_file(filename)

a = 12
