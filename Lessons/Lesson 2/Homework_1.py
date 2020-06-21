# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = [True, "Москва", 15, 10.8, None, ["Опять словарь", 2]]
for position, element in enumerate(my_list, 1):
    print(f"Тип элемента № {position} - {element} - {type(element)}")
