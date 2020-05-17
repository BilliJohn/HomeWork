# считаем учебные часы
from functools import reduce


def study_hour(_x=''):
    _x = _x.split('(')[0]
    return int(_x) if _x.isdigit() else 0


with open('text_5_6.txt', 'r', encoding='utf-8') as my_f:
    _dict = {}
    for _coun in my_f.readlines():
        _x = _coun.strip().split()
        _dict[_x[0].split(':')[0]] = sum(study_hour(_i) for _i in _x)

    print(_dict)
