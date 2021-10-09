import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

import settings
from form import *
from utils import start, help, any_message

logging.basicConfig(filename= "bot.log", level=logging.INFO, filemode= "w")


def main():
    bot = Updater(settings.API_KEY, use_context=True)

    disp = bot.dispatcher

    form = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("^(Создать анкету)$"), form_start),
                      MessageHandler(Filters.regex("^(Изменить анкету)$"), form_start),
                      CommandHandler("anketa", form_start)],
        states={"name": [MessageHandler(Filters.text, form_name)],
                "call": [MessageHandler(Filters.text, form_call)],
                "subjects_know": [MessageHandler(Filters.text, form_subjects_know)],
                "how_know": [MessageHandler(Filters.text, form_how_know)],
                },
        fallbacks=[]
    )

    disp.add_handler(form)
    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("help", help))
    disp.add_handler(MessageHandler(Filters.text, any_message))

    logging.info("bot has started")
    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
