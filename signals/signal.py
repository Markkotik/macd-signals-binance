from abc import ABC, abstractmethod
from typing import Type

import pandas as pd

from models.signal_model import Signal


class AbstractSignal(ABC):
    """
    Abstract class for signals. It provides the blueprint for signal identification methods.
    """

    @abstractmethod
    def identify_signal(self, data: pd.DataFrame) -> Type[Signal]:
        """
        Analyzes the given data, applies necessary signal calculations, and identifies the signal.

        :param data: The data in which to analyze and detect the signal.
        :return: An instance of the Signal class with attributes indicating the time,
                 symbol, timeframe, indicator name, and the detected direction
                 ('buy', 'sell', or 'none').
        """
        pass
