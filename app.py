import telebot


TOKEN = "5925054606:AAFCQUuX-y2UxpW8NYQk2YAxkPxYRrPgRhQ"


bot = telebot.Telebot(TOKEN)


@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'hello')


bot.polling()