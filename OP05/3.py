#1. Возьми одну из программ, которую мы писали на прошлых уроках, продумай, какие ошибки в программе могут появляться(можно прям специально пробовать ее ломать) 
#и дополни код конструкцией try-except для обработки выявленных исключений.

try:
    a = float(input('Введите число a: '))
    b = float(input('Введите число b: '))
except:
    print('Некорректный ввод')
else:
    op = input('Введите операцию: (+, -. *, /): ')
    if op == '+':
        c = a + b
        print( a, '+', b, '=', c)
    elif op == '-':
        c = a - b
        print( a, '-', b, '=', c)
    elif op == '*':
        c = a * b
        print( a, '*', b, '=', c)
    elif op == '/':
        c = a / b
        print( a, '/', b, '=', c)
    else: 
        print('Вы ввели некорректный символ')