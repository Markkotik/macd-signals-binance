from abc import ABC, abstractmethod
from typing import Literal

import pandas as pd


class AbstractSignal(ABC):
    """
    Abstract class for signals.
    """

    @abstractmethod
    def identify_signal(self, data: pd.DataFrame) -> Literal['buy', 'sell', 'none']:
        """
        Analyzes the given data, applies necessary signal calculations, and identifies the signal.

        :param data: The data in which to analyze and detect the signal.
        :return: 'buy' if a buy signal is detected,
                 'sell' if a sell signal is detected,
                 'none' otherwise.
        """
        pass
