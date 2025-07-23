# main.py

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TOKEN

def start(update: Update, context: CallbackContext):
    # keyboard yaratish va xabar jo'natish
    ...

def handle_message(update: Update, context: CallbackContext):
    # xabarlarni qabul qilish va javob berish
    ...

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

