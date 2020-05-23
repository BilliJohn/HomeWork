class Road:
    __length = 0
    __width = 0

    def __init__(self, ll, ww):
        self.__length = ll  # метры
        self.__width = ww   # метры

    def brutto(self, heigh=1, density=1):
        return density * (self.__width * self.__length) * heigh / 1000


# проверка
a = Road(5000, 20)
print(f'Потребуется : {a.brutto(5, 25)} тонн асфальта ')

