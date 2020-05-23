
import time


class TrafficLight:
    __color = ''

    def __init__(self):
        self.time_on = time.time()    # время первого включения светофора
        self.light = (['красный', 7], ['желтый', 2], ['зеленый', 5])  # цикл светофора
        self.time_cycle = sum(count_var[1] for count_var in self.light)   # продолжительность 1 цикла переключений

    def running(self):
        current_cycle_time = (int(time.time() - self.time_on)) % self.time_cycle  # время текущего цикла переключений
        for count_var in self.light:
            current_cycle_time = current_cycle_time - count_var[1]   # проверяем на каком цвете находимся
            if current_cycle_time <= 0:
                self.__color = count_var[0]     # присваиваем цвет
                break
        return self.__color


# проверка светофора
a = TrafficLight()
cycle_num = a.time_cycle * 3     # количество опросов светофора
while cycle_num > 0 and not time.sleep(1):     # опрашиваем каждую секунду
    print(f'{cycle_num}: {a.running()}')
    cycle_num -= 1
