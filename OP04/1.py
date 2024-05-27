#1. Напишите функцию sum_range(start, end), которая суммирует все целые 
#числа от значения start до величины end включительно.

import math

def sum_range(beg, end):
    sum = 0
    for i in range(beg,end+1):
        sum += i
    return sum

beg_f = float(input('Введите начало диапазона: '))
beg = math.ceil(beg_f)

end_f = float(input('Введите конец диапазона: '))
end = math.floor(end_f)

print('Сумма ЦЕЛЫХ чисел диапазона: ', sum_range(beg, end))

    
