#Задание 2. Создание модуля с функциями арифметики№
#Создайте модуль arithmetic.py, который будет содержать 4 функции: сложение, вычитание,
#умножение и деление. Импортируйте модуль в другой файл Python и выполните каждую из функций с произвольными аргументами.

def summa(a,b):
    try:
        r = float(a)+float(b)
        return r
    except:
        return None
    
def mult(a,b):
    try:
        r = float(a) * float(b)
        return r
    except:
        return None

def difr(a,b):
    try:
        r = float(a)-float(b)
        return r
    except:
        return None
    
def div(a,b):
    try:
        r = float(a)/float(b)
        return r
    except:
        return None

    
    
