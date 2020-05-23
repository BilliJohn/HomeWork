class Stationery:
    title = 'STATIONERY'

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):

    def __init__(self):
        self.title = 'PEN'

    def draw(self):
        return f'пишем - {self.title} '


class Pencil(Stationery):

    def __init__(self):
        self.title = 'PENCIL'

    def draw(self):
        return f'штрихуем - {self.title} '


class Handle(Stationery):

    def __init__(self):
        self.title = 'HANDLE'

    def draw(self):
        return f'выделяем - {self.title} '


s = Stationery()
p = Pen()
ps = Pencil()
h = Handle()

print(s.draw())
print(p.draw())
print(ps.draw())
print(h.draw())