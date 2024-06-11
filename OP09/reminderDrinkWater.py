import telebot
import datetime
import time
import threading
import random

TOKEN_API = '7148517072:AAHTNP4rSXSVO9YuOoiqtZGo7JVWArtcZok'

bot = telebot.TeleBot(TOKEN_API)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет, я напоминаю Вам о необходимости пить воду')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def start_message(message):
           
    list = ["Вода на Земле может быть старше самой Солнечной системы: Исследования показывают, что от 30% до 50% воды в наших океанах возможно присутствовала в межзвездном пространстве еще до формирования Солнечной системы около 4,6 миллиарда лет назад.",
    "Горячая вода замерзает быстрее холодной: Это явление известно как эффект Мпемба. Под определенными условиями горячая вода может замерзать быстрее, чем холодная, хотя ученые до сих пор полностью не разгадали механизм этого процесса.",
    "Больше воды в атмосфере, чем во всех реках мира: Объем водяного пара в атмосфере Земли в любой момент времени превышает объем воды во всех реках мира вместе взятых. Это подчеркивает важную роль атмосферы в гидрологическом цикле, перераспределяя воду по планете."]
    random_fact = random.choice(list) 
    bot.reply_to(message, f'Вот один из фактов о воде: {random_fact}')

def send_reminders(chat_id):
    first_rem = '21:24'
    second_rem = '14:00'
    end_rem = '18:00'
    while True:            
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or  now == second_rem or now == end_rem:
            bot.send_message(chat_id, f'Настало {now}. Пора выпить стакан воды')
            time.sleep(61)
        time.sleep(1)

    

    
bot.polling(none_stop = True)