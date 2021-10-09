import settings
from emoji import emojize
from keyboards import start_keyboard


def start(update, contex):
    smile = emojize(settings.EMOJI[1], use_aliases=True)
    update.message.reply_text(f"Привет! Я бот, который подберет тебе помощника по проблемным предметам . Начнём? "
                              f"{smile}", reply_markup=start_keyboard())


def help(update, contex):
    update.message.reply_text("/start - запустить бота\n/help - получить список команд\n/anketa - создать анкету"
                              "\n/edit_anketa - изменить анкету\n/search - найти друга")


def any_message(update, contex):
    text = update.message.text
    update.message.reply_text("Я не понимаю тебя. Напиши /help")
