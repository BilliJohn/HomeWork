
class Worker:
    name = ''
    surname = ''
    position = ''
    __income = {"wage": 200, "bonus": 50}

    def __init__(self, nn='', ss='', pp=''):
        self.name = nn
        self.surname = ss
        self.position = pp

    def inc(self, what='wage'):
        return self.__income[what]


class Position(Worker):

    def get_full_name(self):
        return f'ФИО : {self.name} {self.surname}, должность - {self.position}'

    def get_total_income(self):
        return self.inc() * 12 + self.inc('bonus')


# проверка
a = Position('Иван', 'Петров', 'начальника')
print(a.get_full_name())
print(a.get_total_income())