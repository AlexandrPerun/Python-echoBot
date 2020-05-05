import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["hello"])
def welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}!".format(message.from_user))


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__=='__main__':
    bot.infinity_polling()