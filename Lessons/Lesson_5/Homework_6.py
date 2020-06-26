# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def read_user_file(filename):
    """Открывает файл, читает его построчно, добавляет строки в список file_lines
    :param filename: Принимает имя файла вместе с расширением
    :return: возаращает список прочитаных строк file_lines, при неудаче возвращает ошибку IOError
    """
    try:
        with open(filename, "r", encoding="utf-8") as f_user_obj:
            return f_user_obj.readlines()
    except IOError:
        return IOError


def create_subjects_dict(user_string_list):
    def my_replace(my_string):
        """функция создана как обертка над стандартным методом строк replace, для использования в функции map
        принимает строку, если находит суффиксы  - убирает их
        :param my_string: строка
        :return: возвращает строку без суффиксов
        """
        my_string = my_string.replace("(пр)", "").replace("(л)", "").replace("(лаб)", "")
        return my_string

    subjects = {}
    for el in user_string_list:
        # генерируем список, если элемент равен "-" - отбрасываем этот элемент
        my_list = [x for x in el.split() if x != "-"]
        # прогоняем список через функцию mapб используюя свою обертку над методом строк replace - убираем суффиксы
        my_list_w_o_suffix = list(map(my_replace, my_list))
        # заполняем словарь
        subjects[my_list_w_o_suffix[0]] = sum(map(int, my_list_w_o_suffix[1:]))
    return subjects


user_file_name = "text_6.txt"
result = create_subjects_dict(read_user_file(user_file_name))
# печатаем наш словарь, получаем итерар ключ + значение через метод items()
for key, value in result.items():
    print(f"{key}  {value}")
