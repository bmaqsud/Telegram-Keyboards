import handlers
from telegram.ext import Updater, CommandHandler
from config import TOKEN


def main():
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    # command handler
    dispatcher.add_handler(CommandHandler("start", handlers.start))

    # start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
