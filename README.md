# MACD Signals Binance

Welcome to **MACD Signals Binance**! This tool identifies MACD (Moving Average Convergence Divergence) signals on 
Binance's spot market. It notifies you on Telegram of potential buy/sell opportunities with a MACD chart.

## Prerequisites

- Python ~3.10
- Telegram Bot token and chat ID

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Markkotik/macd_signals_binance
    cd macd_signals_binance
    ```

2. **Set up a virtual environment:**  
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**  
   Rename `.env.sample` to `.env` and provide your Telegram details:

    ```plaintext
    # BINANCE CONFIGURATION
    SYMBOL=ETHUSDT
    TIMEFRAME=1m
    LIMIT=90
   
    # TELEGRAM CONFIGURATION
    TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    TELEGRAM_CHAT_ID=YOUR_TELEGRAM_CHAT_ID
    ```

## Running the bot

1. Activate your virtual environment:  
    ```bash
    source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
    ```

2. Launch the bot:
    ```bash
    python main.py
    ```

The bot will monitor the market using your settings. On detecting a MACD signal (buy or sell), it will send a Telegram notification.

## Caution

Secure your Telegram token and chat ID. Don't publicly expose them.

## License

This project is licensed under the MIT License.
