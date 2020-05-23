#  Подсчет строк, букв *

with open('text_5_2.txt', 'r', encoding='utf-8') as my_f:
    input_string = my_f.readlines()
    print(f'Количество строк : {len(input_string)}')
    for _coun, _coun2 in enumerate(input_string):
        print(f'Строка {_coun+1} : {len(_coun2.strip())} симв.')
