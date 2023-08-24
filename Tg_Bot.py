import telebot

bot = telebot.TeleBot("6544804429:AAH5Z_YhVcZgl7pBwNiuz_17wF7cIlxMhbA")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Всем привет! Я готов удалять сообщения, если на них ответят 'удалить'.")

@bot.message_handler(func=lambda message: message.reply_to_message and message.text.lower() == 'удалить')
def handle_delete(message):
    bot.delete_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id)
    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

bot.polling()