#2. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа, после return перечислить 
#все значения через запятую): периметр квадрата, площадь квадрата и диагональ квадрата.

import math

def square(side_length):

    perimeter = 4 * side_length

    area = side_length ** 2
    
    diagonal = side_length * math.sqrt(2)
    
    return perimeter, area, diagonal

side = float(input("Сторона квадрата: "))

result = square(side)

print("Периметр: ", result[0],"\n", "Площадь: ", result[1], "\n", 'Диагональ: ', result[2]) 