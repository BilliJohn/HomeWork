
class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, ss=0, cc='', nn='', ii=False):
        self.speed = ss
        self.color = cc
        self.name = nn
        self.is_police = ii


    def go(self):
        return self.name+' GO'

    def stop(self):
        return self.name+' STOP'

    def turn(self, direction='forward'):
        return self.name+' '+direction

    def show_speed(self):
        return f' скорость - {self.speed}'

    def __str__(self):
        return f'Наименование - {self.name}, цвет - {self.color}{", полиция" if self.is_police else "" }, {self.show_speed()}'


class TownCar(Car):

    def show_speed(self):
        return f' скорость {self.speed if self.speed <= 60 else str(self.speed) + ", Превышение скорости 60 км/ч !"}'


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        return f' скорость - {self.speed if self.speed <= 40 else str(self.speed) + ", Превышение скорости 40 км/ч !"}'


class PoliceCar(Car):
    pass

# проверка


police = PoliceCar(80, 'blue', 'Ford', True)
work = WorkCar(35, 'orange', 'ZIL', False)
town = TownCar(55, 'yellow', 'Honda', False)
sport = SportCar(200, 'red', 'Reno', False)

print(police)
print(work)
print(town)
print(sport)

print(sport.go())
print(police.stop())
print(work.turn('Left'))

work.speed = 70
print(work)

town.speed = 80
print(town)


