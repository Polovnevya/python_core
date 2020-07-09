# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


from abc import ABC, abstractmethod
import json


class Warehouse:
    def __init__(self, number, address):
        self.number = number
        self.address = address


class OfficeEquipment(ABC):
    def __init__(self, inventory_number: int, brand: str, model: str, paper_size: str, warehouse_number: int):
        self.inventory_number = inventory_number
        self.brand = brand
        self.model = model
        self.paper_size = paper_size
        self.warehouse_number = warehouse_number


class Printer(OfficeEquipment):
    def __init__(self, inventory_number: int, brand: str, model: str, paper_size: str, warehouse_number: int,
                 tray_number: int):
        super().__init__(inventory_number, brand, model, paper_size, warehouse_number)
        self.tray_number = tray_number

    @property
    def get_full_info(self):
        return f"производитель {self.brand}, модель {self.model}, размер лотка {self.paper_size}," \
               f" количество лотков {self.tray_number}, инвентаный номер {self.inventory_number}" \
               f" место расположения {self.warehouse_number}"


class Scanner(OfficeEquipment):
    def __init__(self, inventory_number: int, brand: str, model: str, paper_size: str, warehouse_number: int,
                 Optical_Resolution: str):
        super().__init__(inventory_number, brand, model, paper_size, warehouse_number)
        self.Optical_Resolution = Optical_Resolution

    @property
    def get_full_info(self):
        return f"производитель {self.brand}, модель {self.model}, размер принимаемой бумаги {self.paper_size}," \
               f" оптическое разрешение {self.Optical_Resolution}, инвентаный номер {self.inventory_number}" \
               f" место расположения {self.warehouse_number}"


class MultifunctionPrinter(OfficeEquipment):
    def __init__(self, inventory_number: int, brand: str, model: str, paper_size: str, warehouse_number: int,
                 Optical_Resolution: str, tray_number: int):
        super().__init__(inventory_number, brand, model, paper_size, warehouse_number)
        self.Optical_Resolution = Optical_Resolution
        self.tray_number = tray_number

    @property
    def get_full_info(self):
        return f"производитель {self.brand}, модель {self.model}, размер принимаемой бумаги {self.paper_size}," \
               f" оптическое разрешение {self.Optical_Resolution},  количество лотков {self.tray_number}" \
               f"инвентаный номер {self.inventory_number}, место расположения {self.warehouse_number}"


my_printer = Printer(100, "HP", "1100", "A4", 3, 2)
my_scanner = Scanner(101, "Kodak", "Alaris S2070", "A4", 3, "600 dpi")
my_mfu = MultifunctionPrinter(102, "Xerox", "WorkCentre 3225DNI", "A4", 3, "300 dpi", 1)

my_office_department_warehouse = Warehouse(1, "Красных партизан 18")
my_workshop_department_warehouse = Warehouse(3, "Октябрьская 59")

print(my_printer.get_full_info)
print(my_scanner.get_full_info)
print(my_mfu.get_full_info)