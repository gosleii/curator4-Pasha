import telebot

bot = telebot.TeleBot('6758077677:AAGedodag-qTPXFdAN4X-OgG-DsqXcjIZdk')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['jokes'])
def main(message):
    bot.send_message(message.chat.id, 'Ахахахаха')


@bot.message_handler(commands=['Good'])
def main(message):
    bot.send_message(message.chat.id, 'Пока')


bot.infinity_polling()