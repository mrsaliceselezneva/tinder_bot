import models


def bd_edit_anketa(update, contex):  # изменение анкеты
    user_message = update.message.text
    return


def bd_search(update, contex):  # поиск друга
    user_message = update.message.text
    models.find_person(update.message.from_user.id)
    return
