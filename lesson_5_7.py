# анализ компаний *
import json

with open('text_5_7.txt', 'r', encoding='utf-8') as my_f:
    profit = {}
    average_profit = {}
    for _coun in my_f.readlines():
        _x = _coun.strip().split()
        profit[_x[0].split()[0]] = float(_x[2]) - float(_x[3])
        _i = 0
        _sum = 0
        for _x in profit.keys():
            if profit[_x] >= 0:
                _sum += profit[_x]
                _i += 1
        average_profit['Средняя_прибыль'] = _sum / _i
    output_line = [profit, average_profit]
    print(output_line)

with open('text_5_7_1.json', 'w', encoding='utf-8') as my_f:
    json.dump(output_line, my_f)
