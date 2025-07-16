from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    bot = context.bot

    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text="Salom Botga xush kelibsiz."
    )

