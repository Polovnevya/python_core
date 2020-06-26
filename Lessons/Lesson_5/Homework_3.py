# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

from functools import reduce


def read_user_file(filename):
    """Открывает файл, читает его построчно, добавляет строки в список file_lines

    :param filename: Принимает имя файла вместе с расширением
    :return: возаращает список прочитаных строк file_lines, при неудаче возвращает ошибку IOError
    """
    try:
        with open(filename, "r", encoding="utf-8") as f_user_obj:
            file_lines = f_user_obj.readlines()
            return file_lines
    except IOError:
        return IOError


def convert_list_of_string_2_list_of_dict(user_result):
    """Принимает список строк, производит конвертацию - зарплатную часть приводит к флоат,
     отбрасывает символ перевода строки

    :param user_result: Список строк в формате "фамилия оклад" - "Иванов 23543.12"
    :return: Возвращает список словарей, каждый словарь это отдельный сотрудник
    Ключи словаря
        "Last_name" - фамилия
        "Salary" - оклад в типе float
    при неудаче возвращает ValueError
    """
    employee = {"Last_name": None, "Salary": None}
    employers = []
    for line in user_result:
        try:
            employee["Last_name"] = line.split()[0]
            employee["Salary"] = float(line.split()[1].replace(r"\n", ""))
            employers.append(employee.copy())
        except ValueError:
            return ValueError
    return employers[:]


filename = "text_3.txt"
result = read_user_file(filename)
if result != IOError:
    list_of_employers = convert_list_of_string_2_list_of_dict(result)
    employers_min_salary = [employee for employee in list_of_employers if employee["Salary"] < 20000]
    employee_summ = 0
    for employee in list_of_employers:
        employee_summ += employee["Salary"]

    print(f"Сотрудники имеющие оклад меньше 20 тысяч")
    for employee in employers_min_salary:
        print(employee["Last_name"], employee["Salary"])

    print(f"Средний оклад сотрудников составляет {round(employee_summ / len(list_of_employers), 3)}")
else:
    print("Ошибка доступа к файлу {filename}")
