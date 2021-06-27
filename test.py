import telebot
import config
import random
import numpy

bot = telebot.TeleBot(config.token)

list = ('Осуждаю','Не одобряю','Максимальное осуждение' 'Бан')
pid1 = numpy.random.choice(list,replace=False)

@bot.message_handler(regexp='Слива|груша|яблоко|банан|орех')
def handle_message(message):
    pid = random.choice(list)
    bot.reply_to(message, pid)
@bot.message_handler(content_types='sticker')
def send_sticker(message):
    # Получим ID Стикера
    sticker_id = message.sticker.file_id
    bot.reply_to(message, sticker_id)
bot.polling(none_stop=True)