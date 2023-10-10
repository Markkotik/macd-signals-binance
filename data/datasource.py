from abc import ABC, abstractmethod

import pandas as pd
from decouple import config


class DataSource(ABC):
    """
    Abstract class for data sources.
    """

    def __init__(self):
        self.symbol: str = config('SYMBOL')
        self.timeframe: str = config('TIMEFRAME')
        self.limit: int = config('LIMIT', default=300)

    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        """
        Retrieve data based on the symbol, timeframe, and limit attributes.

        :return: DataFrame with the data.
        """
        pass
