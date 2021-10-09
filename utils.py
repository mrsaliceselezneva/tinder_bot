from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import settings
import models
from emoji import emojize


def start_keyboard(update):
    if models.check_user(update.message.from_user.id):
        return ReplyKeyboardMarkup([["Найти пользователя", "Изменить анкету"]],
                                   one_time_keyboard = True)
    return ReplyKeyboardMarkup([["Создать анкету"]], one_time_keyboard=True)


def subjects_keyboard():
    return ReplyKeyboardMarkup([["Алгебра", "Геометрия", "Информатика"],
                                ["Физика", "Химия"],
                                ["Русский", "Литература"],
                                ["Далее"]])


def yes_no_keyboard():
    return ReplyKeyboardMarkup([["Да", "Нет"]], one_time_keyboard=True)


def how_know_keyboard():
    num = [[], []]
    # for i in range(0, 5):
    #    num[0].append(emojize(settings.EMOJI_NUM[i], use_aliases=True))
    # for i in range(5, 10):
    #    num[1].append(emojize(settings.EMOJI_NUM[i], use_aliases=True))

    for i in range(1, 6):
        num[0].append(i)
    for i in range(6, 11):
        num[1].append(i)
    return ReplyKeyboardMarkup(num)


def start(update, contex):
    smile = emojize(settings.EMOJI[1], use_aliases=True)
    update.message.reply_text(f"Привет! Я бот, который подберет тебе помощника по проблемным предметам . Начнём? "
                              f"{smile}", reply_markup=start_keyboard(update))


def help(update, contex):
    update.message.reply_text("/start - запустить бота\n/help - получить список команд\n/anketa - создать анкету")


def any_message(update, contex):
    text = update.message.text
    update.message.reply_text("Я не понимаю тебя. Напиши /help")
