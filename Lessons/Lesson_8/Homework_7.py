# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex:
    def __init__(self, x: str):
        self.x = self.convert(x)

    @staticmethod
    def convert(x):
        try:
            x = complex(x)
            return x
        except ValueError:
            return f"Ошибка преобразования {x} к комплексному числу"

    def __add__(self, other):
        re = int(self.x.real + other.x.real)
        im = int(self.x.imag + other.x.imag)
        return Complex(f"{re}{im}j")

    def __mul__(self, other):
        re = (self.x.real * self.x.imag) - (other.x.real * other.x.imag)
        im = + (self.x.real * other.x.imag + self.x.imag * other.x.real)
        return Complex(f"{re}{im}j")


my_num1 = Complex("3+j")
my_num2 = Complex("2-3j")
my_num3 = my_num1 + my_num2
print(f"({my_num1.x}) + {my_num2.x} = {my_num3.x}")
my_num4 = my_num1 * my_num2
print(f"({str(my_num1.x)}) * {str(my_num2.x)} = {my_num4.x}")
