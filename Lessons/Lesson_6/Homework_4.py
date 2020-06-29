# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.is_move = False
        self.direction = "Север"

    def go(self):
        if self.is_move:
            print(f"машина уже двигается")
        else:
            self.is_move = True
            print(f"машина начала движение")

    def stop(self):
        if not self.is_move:
            print(f"Машина не двигается в текущий момент")
        else:
            self.is_move = False
            print(f"Машина остановила движение")

    def turn(self, drection):
        self.direction = drection
        if self.is_move:
            return f"Машина движется на {self.direction}"
        else:
            print(f"Машина не двигается в текущий момент")

    def show_speed(self):
        if self.is_move:
            return self.speed
        else:
            return 0

    def show_status(self):
        my_text = f"Машина {self.color} {self.name} " \
                  f"{'движется,' if self.is_move else 'стоит,'}" \
                  f" текущая скорость {self.show_speed()}," \
                  f" направление движения {self.direction if self.is_move else 'отсутствует'}," \
                  f" это {'полицейская' if self.is_police else 'гражданская'} машина"
        return print(my_text)


class TownCar(Car):
    # Вариант 1 - переопределение метода show_speed
    def show_speed(self):
        if self.is_move and self.speed > 60:
            self.speed = 60
            return self.speed
        elif not self.is_move:
            return 0
        else:
            return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    # Вариант 1 - переопределение метода _init_
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.speed > 40:
            self.speed = 40
            print(
                f"Внимание! Для грузовых автомобилей {self.name} максимальная скорость ограничена {self.speed} км/ч \n")


class PoliceCar(Car):
    pass


my_town_car = TownCar(60, "White", "Kia", False)
my_town_car_2 = TownCar(90, "Red", "Mercedes", False)
my_sport_car = SportCar(130, "Yellow", "Jaguar", False)
my_work_car = WorkCar(40, "Green", "Kamaz", False)
my_work_car_2 = WorkCar(60, "Green", "Ural", False)
my_police_car = PoliceCar(90, "Blue", "Ford", True)

my_town_car.show_status()
my_town_car.go()
my_town_car.show_status()
my_town_car.stop()
my_town_car.show_status()

print("* " * 18)

my_town_car_2.show_status()
my_town_car_2.go()
my_town_car_2.show_status()
my_town_car_2.stop()
my_town_car_2.show_status()

print("* " * 18)

my_sport_car.show_status()
my_sport_car.go()
my_sport_car.show_status()
my_sport_car.stop()
my_sport_car.show_status()

print("* " * 18)

my_work_car.show_status()
my_work_car.go()
my_work_car.show_status()
my_work_car.stop()
my_work_car.show_status()

print("* " * 18)

my_work_car_2.show_status()
my_work_car_2.go()
my_work_car_2.show_status()
my_work_car_2.stop()
my_work_car_2.show_status()

print("* " * 18)

my_police_car.show_status()
my_police_car.go()
my_police_car.show_status()
my_police_car.stop()
my_police_car.show_status()
