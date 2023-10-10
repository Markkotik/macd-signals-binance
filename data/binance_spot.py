import pandas as pd
from binance.spot import Spot
from .datasource import DataSource


class BinanceSpotDataSource(DataSource):
    def __init__(self):
        """Initializes the Binance Spot client."""
        super().__init__()
        self.client: Spot = Spot()

    def get_data(self) -> pd.DataFrame:
        """
        Retrieves TOHLC (time, open, high, low, close) data from Binance based on the symbol,
        timeframe, and limit attributes.

        :return: DataFrame with TOHLC data.
        """
        raw_data = self.client.klines(symbol=self.symbol, interval=self.timeframe, limit=self.limit)
        tohlc_data = pd.DataFrame(raw_data).iloc[:, :5]
        tohlc_data.columns = list('TOHLC')
        return tohlc_data
