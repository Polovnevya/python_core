# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


from googletrans import Translator


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


def get_translate(eng_list):
    try:
        my_translator = Translator()
        ru_words = []
        trans_result = (my_translator.translate(eng_list, src='en', dest='ru'))
        for i, word in enumerate(trans_result):
            ru_word = f"{word[0].text.title()} - {i + 1}"
            ru_words.append(ru_word)
        return ru_words
    except:
        return "Error"


def write_2_file(user_filename, user_string):
    """Записть в файл реализована через print
    Если возникает ошибка доступа к файлу возвращает ошибку "IOError"
    :param user_filename: Имя файла для записи, по умолчанию к имени добавляет расширение .txt
    :param user_string: Строка которая будет записываться в файл
    :return: Возвращает ошибку при неудачном обращении к файлу
    """
    try:
        with open(f"{user_filename.split('.')[0]}_ru.txt", "w", encoding="utf-8") as f_user_obj:
            for el in user_string:
                print(el, file=f_user_obj)
    except IOError:
        return IOError


filename = "text_4.txt"
result = read_user_file(filename)
ru_result = get_translate(result)
write_2_file(filename,ru_result)