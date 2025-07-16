from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    bot = context.bot

    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text="Salom Botga xush kelibsiz.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton('Mahsulotlar'), KeyboardButton("Buyurtmalarim")],
                [KeyboardButton('Contact', request_contact=True), KeyboardButton("Location", request_location=True)],
            ],
            resize_keyboard=True,
        )
    )

