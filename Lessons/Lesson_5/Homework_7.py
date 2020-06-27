# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json


def read_user_file(user_filename):
    """Открывает файл, читает все строки за раз, добавляет строки в список file_lines

    :param user_filename: Принимает имя файла вместе с расширением
    :return: возаращает список прочитаных строк file_lines, при неудаче возвращает ошибку IOError
    """
    try:
        with open(user_filename, "r", encoding="utf-8") as f_user_obj:
            file_lines = f_user_obj.readlines()
            return file_lines
    except IOError:
        return IOError


def convert_list_of_string_2_list_of_dict(user_result):
    """производит конвертацию списка стров в список словарей
        :param user_result: принимает список строк
        Ключи словаря
        "Firm_name": Название фирмы
        "Type_of_ownership": тип собственности
        "Earnings": Выручка
        "Costs": Затраты
    :return: возвращает список словарей при успехе, иначе ValueError
    """
    firm = {"Firm_name": None,
            "Type_of_ownership": None,
            "Earnings": None,
            "Costs": None}
    firms = []
    for line in user_result:
        try:
            firm["Firm_name"] = line.split()[0]
            firm["Type_of_ownership"] = line.split()[1]
            firm["Earnings"] = float(line.split()[2])
            firm["Costs"] = float(line.split()[3].replace(r"\n", ""))
            firms.append(firm.copy())
        except ValueError:
            return ValueError
    return firms[:]


filename = "text_7.txt"
result = read_user_file(filename)
if result != IOError:
    # Получаем словарь с словарями содержащими фирмы
    list_of_firms = convert_list_of_string_2_list_of_dict(result)
    # В генераторе отбрасываем фирмы имеющие прибыль меньше нуля
    profit_firms = [firm for firm in list_of_firms if (firm["Earnings"] - firm["Costs"]) > 0]
    # объявляем структуры - словарь с фирмами и их прибылями, а также словарь со средней прибылью.
    profit_dict = {}
    average_profit = {"average_profit": None}
    # Временная переменная, храним там прибыль всех фирм с положительной прибылью -
    # требуется для вычисления average_profit
    firms_sum = 0
    # смотрим все фирмы с положительной прибылью, суммируем прибыль, вычисляем среднюю прибыль
    for firm in profit_firms:
        firms_sum = firms_sum + (firm["Earnings"] - firm["Costs"])
    average_profit["average_profit"] = firms_sum / len(profit_firms)
    # смотрим все фирмы вычисляем прибыль - отрицатеьную в том числе
    for firm in list_of_firms:
        profit_dict[firm["Firm_name"]] = (firm["Earnings"] - firm["Costs"])
    # формируем список включающий в себя 2 словаря
    # profit_dict - {"Имя_фирмы": прибыль} прибыль в том числе отрицательная
    # average_profit - средняя прибыль, высчитывалась без учета фирм с отрицательной прибылью
    my_firm_list = [profit_dict, average_profit]
    # Производим сериализацию в формат json и записываем в файл
    with open(f'{filename.split(".")[0]}.json', "w", encoding="utf-8") as my_file:
        json.dump(my_firm_list, my_file, indent=4)
