#  Обработка чисел *
import random
from functools import reduce


def my_func(_a, _b):
    return int(_a) + int(_b)


# создадим программно исходные данные
with open('text_5_5.txt', 'w', encoding='utf-8') as my_f:
    my_f.write(f'{"".join([" "+str(random.randint(1, _i)) for _i in range(300,350)])}')

with open('text_5_5.txt', 'r', encoding='utf-8') as my_f:
    print(f' Сумма чисел : {reduce(my_func, my_f.read().split())}')
