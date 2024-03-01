from telebot import TeleBot

bot = TeleBot("6878848160:AAH6QkZs5ecP8gxg7Ym9IxZcpj3uUdVYpns")

@bot.message_handler(commands=["start"])
def start(messege):
    chat_id = messege.chat.id
    bot.send_message(chat_id, "salom")


bot.polling()
