import telebot

# Замініть "ВАШ_ТОКЕН" на токен, який вам видав BotFather у Telegram
TOKEN = "7352613060:AAEo0oY_C2yQfYvqjvhj2N1yMX2d0_FtjjE"
bot = telebot.TeleBot(TOKEN)

# Обробник команди /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт!")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущений і чекає на повідомлення...")
    bot.infinity_polling()