#  Обработка зарплат *

with open('text_5_3.txt', 'r', encoding='utf-8') as my_f:
    input_string = my_f.readlines()
    print(f'Количество сотрудников : {len(input_string)}\n')
    print('Меньше 20 т.р. получают : ')
    _y = 0
    for _coun in input_string:
        _x = _coun.split()
        if float(_x[1]) <= 20000:
            print(f'    {_x[0]} - {_x[1]} руб.')
        _y = _y + float(_x[1])
    print(f'\nСредняя ЗП : {round(_y/len(input_string),2)} руб. ')