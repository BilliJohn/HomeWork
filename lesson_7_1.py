"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, list_of_lists=None):
        if list_of_lists:
            self.table = list_of_lists
        else:
            self.table = []

    def __str__(self):
        rez = ' '
        for _ii in self.table:
            rez = rez + f'[{", ".join(map(str, _ii))}]\n '
        return rez

    def __add__(self, other):
        rez = Matrix()
        for _ii, x in enumerate(self.table):
            rez.table.append([])
            for _jj, y in enumerate(x):
                rez.table[_ii].append(y + other.table[_ii][_jj])
        return rez


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

c = a + b
print(a)
print(b)
print(c)
