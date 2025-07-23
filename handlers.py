from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
from config import TOKEN

print(TOKEN)
def start(update: Update, context: CallbackContext):
    bot = context.bot

    user = update.effective_user

    bot.send_message(
        chat_id=user.id,
        text="Salom Botga xush kelibsiz.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton('Frtontend dasturlar'), KeyboardButton("Backent dasturlar"), KeyboardButton("No Code dasturlari")],
                [KeyboardButton("Dizaynerlik dasturlari"), KeyboardButton("Database"), KeyboardButton("Android")],
                [KeyboardButton("Bog'lanish")]
            ],
            resize_keyboard=True,
        )
    )

def handle_message(update: Update, context: CallbackContext):
    text=update.message.text
        
    if text == 'Frontend dasturlar':
            frontend_keyboard = [
                [KeyboardButton("HTML")],
                [KeyboardButton("CSS")],
                [KeyboardButton("JavaScript")],
                [KeyboardButton("Orqaga")]
            ]
            reply_markup = ReplyKeyboardMarkup(frontend_keyboard, resize_keyboard=True)
            update.message.reply_text("Frontend dasturlarni tanlang:", reply_markup=reply_markup)

    elif text == 'Backend dasturlar':
            backend_keyboard = [
                [KeyboardButton("Python")],
                [KeyboardButton("Django")],
                [KeyboardButton("FastAPI")],
                [KeyboardButton("Orqaga")]
            ]
            reply_markup = ReplyKeyboardMarkup(backend_keyboard, resize_keyboard=True)
            update.message.reply_text("Backend dasturlarni tanlang:", reply_markup=reply_markup)