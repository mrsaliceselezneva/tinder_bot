from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def start_keyboard():
    return ReplyKeyboardMarkup([["Найти друга", "Создать анкету", "Изменить анкету"]], one_time_keyboard=True)


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


def course_keyboard():
    num = [[], []]
    for i in range(1, 4):
        num[0].append(i)
    for i in range(4, 7):
        num[1].append(i)
    return ReplyKeyboardMarkup(num, one_time_keyboard=True)


def class_keyboard():
    num = [[], []]
    for i in range(5, 9):
        num[0].append(i)
    for i in range(9, 11):
        num[1].append(i)
    return ReplyKeyboardMarkup(num, one_time_keyboard=True)


def school_university_keyboard():
    return ReplyKeyboardMarkup([["Университет", "Школа"]], one_time_keyboard=True)
