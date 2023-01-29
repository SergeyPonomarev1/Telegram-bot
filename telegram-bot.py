import telebot

bot_token = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()