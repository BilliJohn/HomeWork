"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). В классе
 должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
умножение (mul()), деление (truediv()).Данные методы должны применяться только к клеткам и выполнять увеличение,
 уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно
 осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
 двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
 ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
 позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n равно переданному аргументу.
 Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: **\n\n.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: **\n\n***.
Подсказка: подробный список операторов для перегрузки доступен по ссылке."""


class Cell:
    def __init__(self, _q=0):
        self.c_q = _q

    def __add__(self, other):
        _new = Cell()                       # новая клетка
        _new.c_q = self.c_q + other.c_q
        return _new

    def __sub__(self, other):
        _new = Cell()  # новая клетка
        _new.c_q = self.c_q - other.c_q
        if _new.c_q < 0:
            _new.c_q = 0
            print('Ошибка вычитания')
        return _new

    def __mul__(self, other):
        _new = Cell()  # новая клетка
        _new.c_q = self.c_q * other.c_q
        return _new

    def __truediv__(self, other):
        _new = Cell()  # новая клетка
        _new.c_q = self.c_q // other.c_q
        return _new

    def __str__(self):
        return f'(ID {id(self)} : {self.c_q} ячеек)'

    def make_order(self, _o):
        _rez = f'\nДеление по рядам {self.c_q} на {_o}: \n'
        _rez += '\n'.join([''.join(['*' for _i in range(_o)]) for _j in range(self.c_q // _o)])
        _rez += ('\n'+''.join(['*' for _i in range(self.c_q % _o)]) if (self.c_q % _o) != 0 else '')
        return _rez


a = Cell(17)
b = Cell(10)
print(a, b)

_x = a + b
print(f'a + b = {str(_x)}')

_x = a * b
print(f'a * b = {str(_x)}')

_x = a - b
print(f'a - b = {str(_x)}')
_x = b - a

_x = a / b
print(f'a / b = {str(_x)}')
_x = b / a
print(f'a / b = {str(_x)}')

print(a.make_order(5))
print(b.make_order(3))
