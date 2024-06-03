#Задание 1. Создание и запись в файл
#Напишите скрипт, который запрашивает у пользователя текст, а затем записывает этот текст в файл user_data.

user_input = input("Введите текст: ")

with open('c:/Python/Projects/Python_with_Chat_GPT/OP06/user_data.txt', 'w') as file:
    
    file.write(user_input)

print("Текст успешно записан в файл user_data.txt")
