# задание к уроку 3

# 1. Реализовать функцию, принимающую два числа

def my_division(x=0, y=1):
    try:
        return x / y
    except ZeroDivisionError:
        return None
    else:
        return None

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
def my_user(uname='', usurname='', year='', town='', mail='', phone=''):
    my_var = f'{uname} {usurname} {year} {town} {mail} {phone}'
    print(my_var)
    return

# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
def my_func(x=0, y=0, z=0):
    if x < y and x < z:
        return y + z
    elif y < z and y < z:
        return x + z
    else:
        return x + y

# Программа принимает действительное положительное число x и целое отрицательное число y.
def my_mult(x=0, y=-1):
    x = round(x)
    y = round(y)
    return x ** y

# Реализовать функцию int_func(), принимающую слово из маленьких
def my_upper (x = ''):
    return x.capitalize()

def input_number():
    num_string = input('Введите цифры через пробел : ')
    num_string = num_string.split(' ')
    global my_summa
    for count_var in num_string:
       if count_var.isdigit():
           my_summa += int(count_var)
       elif count_var == 'q' or count_var == 'Q':
           return False
    return True


# 2.1
print(my_division(25, 5))
# 2.2
my_user(uname='Игорь', usurname='Петров', year='2010', town='Ростов', mail='123@mm.com', phone='000-00-00')
# 2.3
print(my_func(2, 1, 3))
# 2.4
print(my_mult(134, -1))
# 2.6
print(my_upper('dfDdsa'))

# 2.5
my_summa = 0
while True:
    if input_number():
        print(f'Промежуточная сумма : {my_summa}')
    else:
        break
print(f'ИТОГО : {my_summa}')

