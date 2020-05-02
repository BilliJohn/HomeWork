# coding: utf-8

# п1 проверка типов элементов

list_var = ['строка', 20, 36.6, ['01', '02'], '\u2660']
for count_var in list_var:
    print(type(count_var), end='')
print()

 # п2 меняем местами элементы списка

list_var = list(input('Введите текст : '))
for count_var in range(len(list_var) // 2):
    list_var[count_var * 2], list_var[count_var * 2 + 1] = list_var[count_var * 2 + 1], list_var[count_var * 2]

print(str(list_var))

# п3 времена года

seasone_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето',
           'осень', 'осень', 'осень', 'зима']
seasone_dict = {'зима':[12,1,2], 'весна':[3,4,5], 'лето':[6,7,8], 'осень':[9,10,11]}

month_number = int(input('Введите номер месяца (1-12) : '))
if 0 < month_number <= 12:
    print(f'По списку это  : {seasone_list[month_number-1]}!')
    for count_var in seasone_dict.keys():
        if month_number in seasone_dict.get(count_var):
            print(f'По словарю это : {count_var}!')
            break
else:
    print('Ой! все ..')

# п4 обработка строки

input_str = input('Введите слова, разделяя их пробелами : ')
input_str = input_str.split(' ')
print(f'{count_var+1} {input_str[count_var] if len(input_str[count_var])<10 else input_str[count_var][:10]}')
for count_var in range(len(input_str)):
    pass

# п5 отрабатываем рейтинг

raiting_value = int(input('Введите рейтинг (число) : '))
raiting_list = [7, 5, 3, 3, 2, 2, 2]
raiting_list.sort(reverse=True)
for count_var in range(len(raiting_list)):
    if raiting_value >= raiting_list[count_var]:
        raiting_list.insert(count_var, raiting_value)
        break
    elif count_var == len(raiting_list)-1:
        raiting_list.append(raiting_value)
print(raiting_list)
