import telebot

token = '401772666:AAHcnkge02VRChq5pyrWn1_IQynNA9ACq_M'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет!")


bot.polling(none_stop=False)