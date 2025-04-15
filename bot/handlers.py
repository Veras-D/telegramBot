from telegram.ext import CommandHandler

def start(update, context):
    update.message.reply_text('Hello! I will tell you BTC price every minute!')

start_handler = CommandHandler('start', start)

