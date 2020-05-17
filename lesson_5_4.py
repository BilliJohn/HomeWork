#  Обработка языка *
def num_rus(_x=1):
    _y = 'Один'
    _x = _x if 1 <= _x <= 4 else 1  # проверим вход
    if _x == 2:
        _y = 'Два'
    elif _x == 3:
        _y = 'Три'
    elif _x == 4:
        _y = 'Четыре'
    return _y


with open('text_5_4_1.txt', 'r', encoding='utf-8') as my_f:
    intput_string = my_f.readline()
    output_string = []
    while intput_string:
        _z = intput_string.split()
        output_string.append(f'{num_rus(int(_z[2]))} {_z[1]} {_z[2]}\n')
        intput_string = my_f.readline()

with open('text_5_4_2.txt', 'w', encoding='utf-8') as my_f:
    my_f.writelines(output_string)
