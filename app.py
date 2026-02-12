import os
import telebot

print("Starting app...")

TOKEN = os.getenv("TELEGRAM_TOKEN")

print("Token value is:", TOKEN)

if not TOKEN:
    print("TOKEN IS NONE — EXITING")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is live 🚀")

print("Bot starting polling...")

bot.infinity_polling()
