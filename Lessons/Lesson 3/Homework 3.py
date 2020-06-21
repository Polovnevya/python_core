# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(first, second, third):
    """Принимает 3 агрумента, ищет минимальный и отбрасывает его, возвращает сумму двух оставшихся

    :param first: первый агрумент
    :param second: второй аргумент
    :param third: третий аргумент
    :return: возвращает сумму аргументов sum(my_list), оставшихся в списке my_list после удаления минимального элемента
    """
    my_list = [int(first), int(second), int(third)]
    my_list.pop(my_list.index(min(my_list)))
    return sum(my_list)


while True:
    try:
        my_data = list(input(f"Введите 3 числа разделеных запятыми ").split(','))
        if len(my_data) == 3:
            for _ in my_data:
                if not _.isnumeric() and not abs(int(_)):
                    print(f"{_} не является числом")
                    break
            print(f"Сумма двух наибольших элементов равна {my_func(my_data[0], my_data[1], my_data[2])}")
            break
    except IndexError:
        print(f"Ошибка выполнения функции {IndexError}, введите корректные данные")
