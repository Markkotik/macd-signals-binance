from typing import Optional

import requests
from decouple import config

from models.signal_model import Signal
from .notifier import Notifier


class TelegramNotifier(Notifier):
    """Notifier implementation for sending Telegram notifications."""

    BASE_URL = "https://api.telegram.org/bot{}/sendMessage"
    BASE_URL_FILE = "https://api.telegram.org/bot{}/sendPhoto"

    def __init__(self):
        self.token = config('TELEGRAM_BOT_TOKEN')
        self.chat_id = config('TELEGRAM_CHAT_ID')

    def send(self, signal: Signal, image_path: Optional[str] = None) -> None:
        """Send a notification using the Telegram API based on the provided signal.

        If an image_path is provided, sends an image notification. Otherwise, sends a text notification.
        """
        message = self._generate_message(signal)

        if image_path:
            self._send_image(message, image_path)
        else:
            self._send_text(message)

    @staticmethod
    def _generate_message(signal: Signal) -> str:
        """Generates a notification message based on the provided signal."""
        return (f"Time: {signal.time}\n"
                f"Symbol: {signal.symbol}\n"
                f"Timeframe: {signal.timeframe}\n"
                f"Indicator: {signal.indicator_name}\n"
                f"Direction: {signal.direction}")

    def _send_image(self, message: str, image_path: str) -> None:
        """Sends an image to the specified Telegram chat with a given caption."""
        with open(image_path, "rb") as image_file:
            files = {'photo': image_file}
            data = {'chat_id': self.chat_id, 'caption': message}
            requests.post(self.BASE_URL_FILE.format(self.token), files=files, data=data)

    def _send_text(self, message: str) -> None:
        """Sends a text message to the specified Telegram chat."""
        data = {'chat_id': self.chat_id, 'text': message}
        requests.post(self.BASE_URL.format(self.token), data=data)
