# pip install PyTelegramBotAPI

import telebot

bot = telebot.TeleBot('1743507373:AAHf-HmpCjdtv5C1SHu9-4Z2_TDOCJw-hCE')


@bot.message_handlers(commands=['start', ''])
def start(data):
    content = f"{data}"
    bot.send_message(data.chat.id, content, parse_mode='html')
    print(data)


bot.polling(none_stop=True)
