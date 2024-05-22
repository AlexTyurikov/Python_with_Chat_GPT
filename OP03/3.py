#2/ Определение количества дней в месяце: 
#Пользователь вводит номер месяца (1-12). Выведите количество дней в этом месяце, не учитывая високосный год.

month = int(input('Введите номер месяца: '))

if 1 <= month <= 12:
    if month == 1:
        print('31')  # Январь
    elif month == 2:
        print('28')  # Февраль 
    elif month == 3:
        print('31')  # Март
    elif month == 4:
        print('30')  # Апрель
    elif month == 5:
        print('31')  # Май
    elif month == 6:
        print('30')  # Июнь
    elif month == 7:
        print('31')  # Июль
    elif month == 8:
        print('31')  # Август
    elif month == 9:
        print('30')  # Сентябрь
    elif month == 10:
        print('31')  # Октябрь
    elif month == 11:
        print('30')  # Ноябрь
    elif month == 12:
        print('31')  # Декабрь
else:
    print("Неверный номер месяца. Введите число от 1 до 12.")
