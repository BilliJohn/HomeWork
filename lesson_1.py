# !!задание первого урока
# 1. Поработайте с переменными, создайте несколько, выведите на экран,
print('Работаем с переменными.')

var_int = 1
var_str = 'строка'
var_float = 1.1
var_bool = True

var_int = int(input('Введите число  '))
var_float = float(input('Введите дробь  '))
var_str = input('Введите строку  ')

print(f'Целое : {var_int}; С запятой :{var_float}; Строка : {var_str}; Логическое : {var_bool};')


# 2. Пользователь вводит время в секундах.

print('Преобразуем секунды.')
time_sec = int(input('Введите время (сек) :'))
print(f'{time_sec // 3600} часов {(time_sec % 3600) // 60} минут {time_sec % 60} секунд')


print('Суммируем.')
input_int = str(input('Введите целое число : '))
print(f'Результат {int(input_int) + int(input_int * 2)+int(input_int * 3)}')


# 4. Пользователь вводит целое положительно.
print('Находим наибольшую цифру.')
max_int = 0
input_int = input('Введите целое число : ')
for char_count in input_int:
    if max_int < int(char_count):
        max_int = int(char_count)
print(f'Максимальное число - {max_int}')

# 5. Запросите у пользователя значения выручки

print('Оцениваем компанию.')
input_cash = int(input('Введите размер выручки : '))
input_cost = int(input('Введите размер издержек : '))

if input_cash > input_cost:
    print(f'Компания работает с прибылью! Рентабельность : {round((input_cost - input_cash)* -1 / input_cash,2)} ')
    input_user = int(input('Введите количество сотрудников : '))
    print(f'Прибыль на сотрудника : {round((input_cost - input_cash) * -1 / input_user, 2)} ')
else:
    print(f'Компания работает в убыток! ')

# _________________
print('Работаем со спортсменом.')
input_a = int(input('Введите результат первого дня : '))
input_b = int(input('Введите целевое значение : '))

count_day = 1
if input_a < input_b:
    while input_a < input_b:
        count_day = count_day + 1
        input_a = input_a * 1.1

print(f'Ответ: на {count_day}-й день спортсмен достиг результата - не менее {input_b} км в день.')

