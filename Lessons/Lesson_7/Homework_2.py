# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать
# формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Сlothes(ABC):

    @abstractmethod
    def calculate(self):
        pass


class Coat(Сlothes):
    def __init__(self, size):
        self.size = size

    def calculate(self):
        return f"{round(self.size / 6.5 + 0.5, 3)}"

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 5:
            self.__size = 5
        elif size > 50:
            self.__size = 50
        else:
            self.__size = size


class Suit(Сlothes):
    def __init__(self, height):
        self.height = height

    def calculate(self):
        return f"{round(2 * self.height + 0.3, 3)}"

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 130:
            self.__height = 130
        elif height > 210:
            self.__height = 210
        else:
            self.__height = height


my_coat = Coat(42)
my_suit = Suit(179)

print(f"Для костюма на рост {my_suit.height} требуется {my_suit.calculate()} ткани\n",
      f"Для пальто размера {my_coat.size} требуется {my_coat.calculate()} ткани\n",
      f"Общее количество ткани затраченое на пошив {float(my_suit.calculate()) + float(my_coat.calculate())}")
