import os
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("ERROR: TELEGRAM_TOKEN not found!")
    exit()

print("Token loaded successfully")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 Trading Bot is LIVE and Connected!")

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.reply_to(message, "✅ Bot is running properly.")

print("Bot is starting...")

bot.infinity_polling()
