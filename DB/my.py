import telebot
bot = telebot.TeleBot("8186596632:AAG9DcTfzB1jpr1s2D2AonsGjsFaDzIWCOg")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Hello')

