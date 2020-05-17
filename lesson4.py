from sys import argv
from random import randint
from functools import reduce
from itertools import count, cycle
import math

# расчет ЗП из параметров
_parm = argv[1:]
if len(_parm) > 0:
    _hours, _salary, _bonus = _parm
    print(_hours, _salary, _bonus)
    _k = int(_hours) * int(_salary) + int(_bonus)
    print(f'Вознаграждение : {_k}')

# анализ списка
my_list = [randint(0, 50) for _k in range(25)]
new_list = [_j for _k, _j in enumerate(my_list) if _k == 0 or _j > my_list[_k-1]]
print(f'\nЧисла больше предыдущего')
print(f'Исходный список : {my_list}')
print(f'Результат       : {new_list}')

# диапазон 20 - 240

print(f'\nЧисла кратные 20 или 21 : {[_k for _k in range(20, 240) if _k % 20 == 0 or _k % 21 == 0]}')

# исключение дублей
my_list = [randint(0, 20) for _k in range(20)]
print(f'\nВходят в список один раз')
print(f'Исходный список : {my_list}')
print(f'Результат       : {[_k for _k in my_list if my_list.count(_k) == 1]}')


# произведение всех четных от 100 до 1000
def my_func(_a, _b):
    return _a + _b


print(f'\nСумма четных чисел 100-1000 : {reduce(my_func, [_k for _k in range(100, 1000) if _k % 2 ==0])}')

# итераторы
my_list = []
for _k in count(50):
    if _k > 65:
        break
    else:
        my_list.append(_k)
print(f'\nЦелые числа с 50 ( count() ): {my_list}')

my_list = []
_m = 0
for _k in cycle('ДРЕЙК'):
    if _m > 15:
        break
    else:
        my_list += _k
        _m += 1
print(f'Цикл  ( cycle() ): {my_list}')


# генератор Yield
def my_fact():
    for _x in range(15):
        yield math.factorial(_x)


print(f'\nФакториал 1-15 (yield) {[_k for _k in my_fact()]}')

