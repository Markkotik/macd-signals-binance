from abc import ABC, abstractmethod
from models.signal_model import Signal


class Notifier(ABC):
    """Abstract class to represent a notifier that sends out signals."""

    @abstractmethod
    def send(self, signal: Signal, image_path: str = None):
        """Sends a notification based on the provided signal and an optional image."""
        pass
