import requests
import os
from telegram.ext import CallbackContext
import logging

CHAT_ID = os.getenv("CHAT_ID")
BINANCE_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'

logger = logging.getLogger(__name__)
previous_price = None


def get_btc_price():
    try:
        response = requests.get(BINANCE_API_URL)
        return float(response.json()['price'])
    except Exception as e:
        logger.error(f"Error fetching BTC price: {e}")
        return None


def send_btc_variation(context: CallbackContext):
    global previous_price
    current_price = get_btc_price()

    if current_price is not None:
        if previous_price is not None:
            variation = ((current_price - previous_price) / previous_price) * 100
            emoji = "🟢" if variation >= 0 else "🔴"
            message = (
                f"{emoji} BTC/USDT\n"
                f"💵 Price: ${current_price:,.2f}\n"
                f"📊 Variation: {variation:+.2f}%"
            )
        else:
            message = f"🔍 Start Price: ${current_price:,.2f}"
        previous_price = current_price
    else:
        message = "❌ Error getting BTC price"

    context.bot.send_message(chat_id=CHAT_ID, text=message)


def schedule_price_check(updater):
    job_queue = updater.job_queue
    job_queue.run_repeating(send_btc_variation, interval=60, first=10)

