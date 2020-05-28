from random import shuffle, randint

# константа для отладки
DEBUG_INFO = False
def deb(_str):
    if DEBUG_INFO:
        print(_str)


class Card:
    """ Класс Card: карточка в 3 строки по 5 цифр из разных десятков """
    def __init__(self):
        self.number_test = [_x for _x in range(15)]   # для входа в цикл и дальнейших проверок
        self.number_list = []                         # для удобства печати
        self.check_list =[0, 0, 0]

        # именно так в столотто контролируют, чтобы в карточку не попала выигрышная цифра))
        while 0 in self.number_test or len(set(self.number_test)) != 15:        # нет повторов и 0 не затесался
            self.number_test = []                                               # очистили
            self.number_list = []
            for line_num in range(3):                                           # 3 строки по 5
                _ten_list = [randint(_x, _x + 9) for _x in range(0, 100, 10)]   # берем 10 цифр из каждого десятка
                shuffle(_ten_list)                                              # перемешиваем
                shuffle(_ten_list)                                              # перемешиваем дважды
                _line = _ten_list[0:5]                                          # берем первые 5
                _line.sort()
                self.number_test.extend(_line)
                self.number_list.append(_line)
        # подготовим строки для красивой печати
        for line_num in range(3):               # можно сделать оптимальней, не хочется тратить время
            _z = ''
            for _x in range(0, 100, 10):
                _a = '   '
                for _y in self.number_list[line_num]:
                    if _x <= _y <= _x + 9:
                        _a = str(_y).rjust(3)
                        break
                _z += _a
            self.number_list[line_num] = _z

    def __str__(self):
        _rez = f'-- карта : {id(self)} ----------\n' + '\n'.join(_s for _s in self.number_list) + \
               '\n------------------------------\n'
        return _rez

    def card_check(self, barrel=0):
        _rez = None
        for _coun in range(3):
            if self.number_list[_coun].find(barrel) != -1:
                self.number_list[_coun].replace(barrel, '  *')
                self.check_list[_coun] += 1
                _rez = 'Room' if self.check_list[_coun] ==5 else 'Yes'

        if sum(self.check_list) == 15:    # ПОБЕДА!!!
            _rez = 'WIN'

        return _rez


class Bag:
    """ Класс Bag : Мешок с бочонками от 1 до 99 """
    def __init__(self):
        self.barrel = [str(_var).rjust(3) for _var in range(1, 100)]
        shuffle(self.barrel)    # перемешаем мешок
        shuffle(self.barrel)    # перемешаем мешок
        shuffle(self.barrel)    # перемешаем мешок
        self.history = []                                               # история ходов

    def __str__(self):
        return 'Мешок :\n' + Bag.table(self.barrel) + '\nИстория :\n' + Bag.table(self.history)

    @staticmethod   # печать списка столбиками по 10
    def table(_list=[], _row=10, _tab='       '):
        _var = _tab
        _llen = len(_list)
        _len = _llen // _row + 1 if _llen > 0 else 0  # количество строк
        for _k in range(_len):
            _var += '\t'.join(
                [_list[_row * _k + _z] for _z in range(_row if _k + 1 != _len else _llen % _row)]) + '\n' + _tab
        return _var

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.barrel) != 0:
            _var = self.barrel.pop(0)   # взяли бочку
            self.history.append(_var)   # записали в историю
            return _var
        else:
            raise StopIteration


class GamePlay():
    """Класс GamePlay: игровое поле, мешок + 2 игрока"""
    def __init__(self):
        self.bag = Bag()
        self.comp1 = Card()
        self.comp2 = Card()

    def play(self):
        _rez = -1
        for barrel in self.bag:
            _two = self.comp2.card_check(barrel)
            _one = self.comp1.card_check(barrel)

            if isinstance(_one, str):
                if _one == 'Yes':
                    deb(f'У первого игрока выпал номер {barrel} !')
                elif _one == 'Room':
                    deb(f'У первого игрока квартира !')
                elif _one == 'WIN':
                    deb(f'У первого игрока выпал номер {barrel} !')
                    deb(f'Победил первый игрок !')
                    _rez = 0
                    break

            if isinstance(_two, str):
                if _two == 'Yes':
                    deb(f'У второго игрока выпал номер {barrel} !')
                elif _two == 'Room':
                    deb(f'У второго игрока квартира !')
                elif _two == 'WIN':
                    deb(f'У второго игрока выпал номер {barrel} !')
                    deb(f'Победил второй игрок !')
                    _rez = 1
                    break
        else:
            deb('Бочoнки закончились !!')
        return _rez


# -- исполняемая часть -----------------------------
# -- одна игра
game = GamePlay()
_coun = game.play()
print(f'Победил игрок №{_coun+1} на {len(game.bag.history)} ходу !!\n')
print(game.comp1)
print(game.comp2)
print(game.bag)

# проверяем статистику игр
itaration_num = 100
stat = [0, 0]
win_step = 0
for _x in range(itaration_num):
    game = GamePlay()
    _y = game.play()
    stat[_y] +=1
    win_step += len(game.bag.history)

print(f'Общая статистика на {itaration_num} игр: {stat}, победа в среднем на {round(win_step / (itaration_num - 1))} ходу..')
