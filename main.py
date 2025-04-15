from telegram.ext import Updater
from bot.handlers import start_handler
from bot.price_checker import schedule_price_check
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(start_handler)
    schedule_price_check(updater)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

