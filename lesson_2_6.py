# coding: utf-8
# п6
# ввод данных с экрана делать не стал, ввиду очевидности решения и высокие временные затраты при тестировании
# зато поробовал решить 2-мя способами

goods_list = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
              (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
              (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'}),
              (4, {'название': 'коврик', 'цена': 15, 'количество': 300, 'eд': 'м2'})]

# чистим данные
goods_clear = list()
for count_var in range(len(goods_list)):
    goods_clear.append(goods_list[count_var][1])

# готовим результат
goods_summ = dict()
for count_var in goods_list[1][1].keys():
    goods_summ.update({count_var: {}})

# проходим и собираем значения
for count_var in goods_summ:
    list_val = []
    for count_var1 in range(len(goods_clear)):
        list_val.append(goods_clear[count_var1].get(count_var))
    goods_summ.update({count_var: set(list_val)})

print(f'----- метод перебора \n {goods_summ}  ')

# пробуем через транспонирование матрицы
goods_keys = goods_list[1][1].keys()
goods_for_transp = list()

# выбираем значения

for count_var in range(len(goods_list)):
    goods_for_transp.append(goods_clear[count_var].values())

b = []
for count_var in zip(*goods_for_transp):
    b.append(set(count_var))

print(f"\n----- метод транспонирования матрицы \n {dict(zip(goods_keys, b))}  ")





