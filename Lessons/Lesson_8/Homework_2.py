# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.


class MyOwnErr(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


print(f"Программа производит обработку деления на ноль")
dividend = None
divider = None
try:
    dividend = int(input("Введите делимое "))
    divider = int(input("Введите делитель "))
    if divider == 0:
        raise MyOwnErr("На ноль делить нельзя!")
except ValueError:
    print(f"\nОшибка преобразования к числу")
except MyOwnErr as err:
    print(err)
