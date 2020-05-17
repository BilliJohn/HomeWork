#  запись в файл введенных строк

with open('text_5_1.txt', 'w') as my_f:
    input_string = '*'
    while input_string:
        input_string = input('Введите строку : ')
        my_f.write(input_string+'\n')


