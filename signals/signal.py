from abc import ABC, abstractmethod
from typing import Any

import pandas as pd


class AbstractSignal(ABC):
    """
    Abstract class for signals.
    """

    @abstractmethod
    def detect(self, data: pd.DataFrame) -> Any:
        """
        Detect a specific signal within the given data.

        :param data: The data in which to detect the signal.
        :return: Information about the detected signal.
        """
        pass
