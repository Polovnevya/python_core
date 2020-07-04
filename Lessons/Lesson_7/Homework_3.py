# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических
# операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if (self.nucleus - other.nucleus) > 0:
            return Cell(self.nucleus - other.nucleus)
        else:
            return f"Клетки не могут уменьшиться"

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        try:
            return Cell(self.nucleus // abs(other.nucleus))
        except ZeroDivisionError:
            return f"клетка не может поделиться"

    def make_order(self, row):
        nucleus_str = "*" * self.nucleus
        start = 0
        nucleus_str_arrange = ""
        end = len(nucleus_str)
        for el in range(1, end + 1, row):
            nucleus_str_arrange += f"{(nucleus_str[start:row + start])}\n"
            start += row
        return nucleus_str_arrange


order_num = 5
print(f"Количесво ячек в ряду {order_num}")
my_cell_1 = Cell(9)
my_cell_2 = Cell(4)

my_cell_3 = my_cell_1 + my_cell_2
print(f"Сложение двух клеток,\n"
      f" {my_cell_1.nucleus}\n{my_cell_1.make_order(order_num)}"
      f" и\n"
      f" {my_cell_2.nucleus}\n{my_cell_2.make_order(order_num)}"
      f"=\n"
      f" {my_cell_3.nucleus}\n{my_cell_3.make_order(order_num)}")

print("--*" * 15)

my_cell_3 = my_cell_1 - my_cell_2
print(f"Вычитание двух клеток,\n"
      f" {my_cell_1.nucleus}\n{my_cell_1.make_order(order_num)}"
      f" и\n"
      f" {my_cell_2.nucleus}\n{my_cell_2.make_order(order_num)}"
      f"=\n"
      f" {my_cell_3.nucleus}\n{my_cell_3.make_order(order_num)}")

print("--*" * 15)

my_cell_3 = my_cell_1 * my_cell_2
print(f"Умножение двух клеток,\n"
      f" {my_cell_1.nucleus}\n{my_cell_1.make_order(order_num)}"
      f" и\n"
      f" {my_cell_2.nucleus}\n{my_cell_2.make_order(order_num)}"
      f"=\n"
      f" {my_cell_3.nucleus}\n{my_cell_3.make_order(order_num)}")

print("--*" * 15)

my_cell_3 = my_cell_1 / my_cell_2
print(f"Деление двух клеток,\n"
      f" {my_cell_1.nucleus}\n{my_cell_1.make_order(order_num)}"
      f" и\n"
      f" {my_cell_2.nucleus}\n{my_cell_2.make_order(order_num)}"
      f"=\n"
      f" {my_cell_3.nucleus}\n{my_cell_3.make_order(order_num)}")