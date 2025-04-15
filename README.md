# 🤖 BTC Price Telegram Bot

A simple and modular **Telegram bot** built with Python that tracks the **BTC/USDT** price from Binance and sends periodic updates to your Telegram chat.  
Useful for traders, crypto nerds, or anyone who just wants to keep an eye on Bitcoin without checking charts all the time. 💸📈

---

## 📦 Features

- 🧠 Sends the current BTC price every minute
- 🔄 Shows variation from the previous value with percentage and emoji
- 🔔 Customizable start command (`/start`)
- 🔐 Uses environment variables to keep your token safe
- 🔧 Easy to maintain and extend (clean, modular code)

---

## 📁 Project Structure

```
btc_telegram_bot/
│
├── bot/
│   ├── __init__.py
│   ├── handlers.py         # Handles commands and job scheduling
│   ├── price_service.py    # Fetches price and sends Telegram messages
│
├── .env.example            # Environment variable template
├── .gitignore
├── requirements.txt
├── main.py                 # Entry point
├── README.md
```

---

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/veras-d/telegramBot.git
cd telegramBot
```

### 2. Set up the environment

Create a `.env` file using the provided example:

```bash
cp .env.example .env
```

Then edit it with your bot token and chat ID:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
CHAT_ID=your_chat_id
BINANCE_API_URL=https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
```

> 💡 You can get your chat ID using [@userinfobot](https://t.me/userinfobot) on Telegram.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the bot

```bash
python main.py
```

The bot will start polling and send a message every 60 seconds with the BTC price update. 🚀

---

## 🛠 Tech Stack

- Python 🐍
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Binance API](https://binance-docs.github.io/apidocs/spot/en/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚠️ Disclaimer

This is a personal project made for fun and educational purposes. Always double-check crypto prices from multiple sources before making financial decisions. Not financial advice. 🙃

---

## 📬 Contributions

Pull requests and suggestions are welcome! If you liked it, leave a ⭐️ or fork it and customize it for your own crypto needs.

---

## 📸 Preview

![preview](../public/discordBot/bot-1.png)
