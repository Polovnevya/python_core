# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(first, second):
    """ Производит деление, делает проверку на деление на ноль ZeroDivisionError

    :param first: Делимое
    :param second: Делитель
    :return: Возвращает результат деления
    """
    try:
        result = first / second
        return result
    except ZeroDivisionError:
        print(f"Ошибка деления на ноль!")
        return "Ошибка деления"


a = int(input("Введите делимое "))
b = int(input("Введите делитель "))
print(f"Результат деления {a} на {b} равен {division(a, b)}")
