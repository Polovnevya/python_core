# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, l_matrix):
        self.l_matrix = l_matrix

    def __str__(self):
        my_matrix_str = ""
        for r_index, row in enumerate(self.l_matrix):
            my_matrix_str = "" if (my_matrix_str == "") else my_matrix_str + "\n"
            for c_index, column in enumerate(self.l_matrix[r_index]):
                my_matrix_str = my_matrix_str + f"{column : ^ 5}"
        return str(my_matrix_str)

    def __add__(self, other):
        my_matrix_str = ""
        my_matrix_1 = []
        my_matrix_2 = []
        for r_index, row in enumerate(self.l_matrix):
            my_matrix_str = "" if (my_matrix_str == "") else my_matrix_str + "\n"
            for c_index, column in enumerate(self.l_matrix[r_index]):
                my_matrix_str += f"{(self.l_matrix[r_index][c_index] + other.l_matrix[r_index][c_index])},"
        # жуткий костыль, ибо невнимательно прочитал задание. возвращал строку вместо нового экземпляра класса
        my_matrix_1 = my_matrix_str.split(sep="\n")
        for i in my_matrix_1:
            my_matrix_2.append(i.split(sep=","))
        my_matrix_1=[]
        for i in my_matrix_2:
            my_matrix_1.append(list(map(int, i[:len(i) - 1])))
        #можно выдохнуть, ужасы закончились
        return Matrix(my_matrix_1)


my_matrix_1 = Matrix([[1, 2, 7], [3, 4, 8], [5, 6, 9]])
my_matrix_2 = Matrix([[10, 12, 17], [13, 14, 18], [15, 16, 19]])
my_matrix_3 = my_matrix_1 + my_matrix_2
print(f"проверяем что у нас возвращает результат сложения 2х матриц - "type(my_matrix_3))
print(f"{my_matrix_1}\n+\n{my_matrix_2}\n=\n{my_matrix_1 + my_matrix_2}")
