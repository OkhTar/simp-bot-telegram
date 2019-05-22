import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

# логтрование данных
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(bot, update):
    print(update)
    print("\n")

    user = update.message.chat.first_name
    my_text = """Привет {}!
            
Посмотрим что будет дальше..
    """.format(user)

    update.message.reply_text(my_text)


def chat(bot, update):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)


def main():
    updtr = Updater(settings.TELEGRAM_API_KEY) # экземпляр класса и ключ апи (от самого телеграмма)

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    logging.info('Bot started')
    main()