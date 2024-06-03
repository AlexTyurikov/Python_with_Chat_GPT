#Напишите программу на Python с использованием модуля tkinter, которая позволяет пользователю ввести свое имя в окно ввода, 
#а затем выводит на экран сообщение "Привет, [имя]!".

import tkinter as tk

#функция обрабатывющая нажатие кнопки
def on_but_click():
    
    #считываем текст из формы
    name = input_form.get()
   
    #текст приветствия
    label2 = tk.Label(root, text = f'Здрассте, {name}')
    label2.pack()  

#родительское окно
root = tk.Tk()
root.title('Дратути вам')

#Текстовое поле
label = tk.Label(root, text = 'Ваше имя?')
label.pack()

#Форма для ввода имени
input_form = tk.Entry(root)
input_form.pack()

#Кнопка для считывания текста из формы
but = tk.Button(root, text = 'Нажми меня', command = on_but_click)
but.pack()

#отображение всего
root.mainloop()