# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.


from time import sleep
from colorama import Back


class TrafficLight:
    __color = "Red"

    def __init__(self, red_time=7, yellow_time=2, green_time=10):
        self.green_time = green_time
        self.yellow_time = yellow_time
        self.red_time = red_time

    def running(self):
        def switch_colors():

            for second in range(1, int(self.red_time) + int(self.yellow_time) + int(self.red_time)):
                for red_second in range(1, int(self.red_time) + 1):
                    print(f"{Back.RED}{red_second}", end="", flush=True)
                    sleep(1)
                    TrafficLight.__color = "Red"
                    print("\b\b", end="")
                for yellow_second in range(1, int(self.yellow_time) + 1):
                    print(f"{Back.YELLOW}{yellow_second}", end="", flush=True)
                    sleep(1)
                    TrafficLight.__color = "Yellow"
                    print("\b\b", end="")
                for green_second in range(1, int(self.green_time) + 1):
                    print(f"{Back.GREEN}{green_second}", end="", flush=True)
                    sleep(1)
                    TrafficLight.__color = "Green"
                    print("\b\b", end="")

        switch_colors()


my_light = TrafficLight()
my_light.running()
