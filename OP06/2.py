#Задание 2. Создайте модуль arithmetic.py, который будет содержать 4 функции: сложение, вычитание, умножение и деление. 
#Импортируйте модуль в другой файл Python и выполните каждую из функций с произвольными аргументами.

import aryph

while True:
    a = input('Первый операнд (a) = ')
    b = input('Второй операнд (b) = ')
    oper = input('Введите действие: +, -, *, / : ' )
    if oper == '+':
       print('a + b = ', aryph.summa(a,b))
    elif oper == '-':
      print('a - b = ', aryph.difr(a,b))
    elif oper == '*':
        print('a * b = ', aryph.mult(a,b))
    elif oper == '/':
      print('a / b = ', aryph.div(a,b))
    else:
        print(None)
    
    user_input = input("Введите 'stop' для завершения: ")
    if user_input == 'stop':
        break
    print('Работа продолжена')