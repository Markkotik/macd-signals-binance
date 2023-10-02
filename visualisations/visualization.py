from abc import ABC, abstractmethod

import pandas as pd

from models.signal_model import Signal


class AbstractVisualization(ABC):
    """
    Abstract class for visualization.
    """

    @abstractmethod
    def visualize(self, data: pd.DataFrame, signal_model: Signal) -> str:
        """
        Visualizes the given data based on the provided signal model.

        :param data: The data to visualize.
        :param signal_model: The signal model containing signal details.
        :return: Image path where the visualization is saved.
        """
        pass
