# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


from itertools import count, cycle


# **********************************************************************************************************************
def iter_count(start, stop):
    return list([x for x in range(int(start), int(stop + 1))])


def iter_count_v2(start, stop):
    my_inner_list = list()
    for el in count(start):
        if el > stop:
            break
        else:
            my_inner_list.append(el)
    return my_inner_list


print(iter_count(10, 20))
print(iter_count_v2(10, 20))
# **********************************************************************************************************************
print("* " * 28)

my_dig = [1, 2, 3]
my_str = "Hello! "


def iter_cycle(my_list, stop):
    my_count = 0
    my_inner_list = list()
    for el in cycle(my_list):
        if my_count > stop:
            break
        else:
            my_inner_list.append(el)
            my_count = my_count + 1
    return my_inner_list


print(iter_cycle(my_dig, 10))
print(iter_cycle(my_str, 10))
