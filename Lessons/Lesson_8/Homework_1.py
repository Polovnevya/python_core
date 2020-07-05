# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class MyDate:
    def __init__(self, str_date):
        if isinstance(MyDate.date_splitter(str_date), list):
            self.date = MyDate.date_splitter(str_date)
        else:
            print(MyDate.date_splitter(str_date))

    @classmethod
    def date_splitter(cls, str_date):
        try:
            return cls.date_validator(list(map(int, str_date.split("-"))))
        except ValueError:
            return f"Ошибка преобразования {str_date} к числу"

    @staticmethod
    def date_validator(my_date_list):
        date = my_date_list[0]
        month = my_date_list[1]
        year = my_date_list[2]
        if 0 < date <= 31:
            if 0 < month <= 12:
                return my_date_list
            else:
                return f" Месяц {month} должен быть больше 1 и меньше 12"
        else:
            return f"День {date} должен быть больше 0 и меньше или равен 31"

my_date1 = MyDate("142-10-2020")
my_date2 = MyDate("12-18-2020@!d")
my_date3 = MyDate("1-8-1980")
my_date4 = MyDate("12-10-2020")
print(my_date3.date)
print(my_date4.date)
