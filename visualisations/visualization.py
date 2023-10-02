from abc import ABC, abstractmethod
import pandas as pd


class AbstractVisualization(ABC):
    """
    Abstract class for visualization.
    """

    @abstractmethod
    def visualize(self, data: pd.DataFrame) -> None:
        """
        Visualizes the given data.

        :param data: The data to visualize.
        """
        pass
