#Задача 2: Создайте пустой список и с помощью функций изученных на уроке сначала добавьте в список 3 элемента(числа), после 
#этого вставьте 2 элемента(числа) в самое начало списка и отсортируйте список по убыванию
my_list = []
donor = [21, 22, 23]
if my_list == []:
    print('Список пуст')
my_list.extend(donor)
print('список расширен элементами списка donor: ', donor, '\n', 'результат: my_list = ', my_list)
print('в начало списка добавлены три элемента: ')      
my_list.insert(0, 1)
my_list.insert(1, 2)
my_list.insert(2, 3)
my_list.reverse()
print('результат: my_list = ', my_list)
print('результат: инверсированный my_list = ', my_list)
