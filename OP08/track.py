import tkinter as tk
import datetime

def on_enter(event): #Передача упрвление кнопке 'добаить задачу' по нажатию 'enter'
    add_task()
  
def add_task():
    task = task_entry.get() #здесь мы получаем слова из поля для ввода
    if task: 
        task_listBox.insert(tk.END, task) #здесь с помощью константы END ставляем полученное слово в конец списка
        task_entry.delete(0, tk.END) #здесь очищаем поле для ввода, от нулевого индекса и до конца

def delete_task():
    selected_task = task_listBox.curselection() #с помощью функции curselection элемент, на который мы нажмём, будет передавать свой ID, индекс, в переменную selected_task
    if selected_task:
         task_listBox.delete(selected_task) #удаляем выбранный элемент из списка
         
def mark_task():   
    selected_task = task_listBox.curselection() #с помощью функции curselection элемент, на который мы нажмём, будет передавать свой ID
    if selected_task:
        task_listBox.itemconfig(selected_task, bg = 'grey0', fg = 'White') #с помощью функции itemconfig выполненная задача изменит цвет заливки
        task_listBox.selection_clear(0, tk.END) #Убираем маркер из списка - мешает

#Определение сегдняшней даты
current_date = datetime.datetime.now()
formatted_date = current_date.strftime('%d.%m.%Y')
root = tk.Tk() #Родительское окно
root.title('Task tracker')
root.configure(background = 'FloralWhite')
root.geometry('600x400+200+100')

text1 = tk.Label(root, text = f'Сегодня {formatted_date}г. Определите ваши задачи на сегодня:', bg = 'FloralWhite') #Текст
text1.config(font = ('Currier', 12, 'bold', 'underline')) #Формат текста
text1.pack(pady=10)
task_entry = tk.Entry(root, width=30, bg = 'Ivory2') #создание Entry
task_entry.pack(pady=15)
task_entry.bind('<Return>', on_enter) #Водить задачу пока не нажмется 'enter'
add_task_button = tk.Button(root, text='Добавить задачу', command = add_task)
add_task_button.pack(pady=5)
delete_button = tk.Button(root, text="Удалить задачу", command=delete_task) 
delete_button.pack(pady=5)
mark_button = tk.Button(root, text = 'Отметить выполненную задачу', command = mark_task)
mark_button.pack(pady=5)
task_listBox = tk.Listbox(root, height=10, width=50, bg = 'Ivory2')
task_listBox.pack(pady=10)

root.mainloop()