import telebot
import config
import random
import numpy

bot = telebot.TeleBot(config.token)

list = ['Осуждаю','Не одобряю','Максимальное осуждение']

list1 = ['Слава Украине' , ' Героям Слава']

list2 = ['Максим Пидар', 'Максим соси хуй','в текен будешь?','сасать будешь?','максим пидор']

list3 = ['Давай, пошути еще раз','пук-пук','среньк']


@bot.message_handler(regexp='Пидор|негр|пидорасы|педик')
def handle_message(message):
    pidor = random.choice(list)
    bot.reply_to(message, pidor)

@bot.message_handler(regexp='Украина|хохол|свинья')
def handle_message(message):
    kakol = random.choice(list1)
    bot.reply_to(message, kakol)

@bot.message_handler(regexp='Maxim|Максим|Макс')
def handle_message(message):
    makc = random.choice(list2)
    bot.reply_to(message, makc)

@bot.message_handler(regexp='сквад|врыв')
def handle_message(message):
    squad = random.choice(list3)
    bot.reply_to(message, squad)

@bot.message_handler(regexp='Выкупай|Викупай|Выкупаешь|Выкупает|Викупае')
def handle_message1(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAICOmDYagK4AVfvPsRw0mr7GNDSfsrhAAI2AQACtIBKJPF7rPZ3U6XHIAQ")

bot.polling()