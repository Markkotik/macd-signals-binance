from dataclasses import dataclass

from decouple import config


@dataclass
class Signal:
    """
    Represents a trading signal with various attributes related to the trade.

    Attributes:
    - entry_price (float): The price at which the trade is entered.
    - time (str): Timestamp or time representation when the signal is generated.
    - indicator_name (str): Name of the technical indicator generating the signal (e.g., MACD).
    - direction (str): The direction of the trade (e.g., "buy" or "sell").
    - stop_loss (float): The price at which the trade will be exited to prevent further losses.
    - take_profit_1 (float): The first price target for taking profit.
    - take_profit_2 (float): The second price target for taking profit.
    - take_profit_3 (float): The third price target for taking profit.
    - symbol (str): Trading symbol or ticker. Default is fetched from configuration.
    - timeframe (str): The trading timeframe (e.g., "1H", "1D"). Default is fetched from configuration.
    """

    entry_price: float
    time: str
    indicator_name: str
    direction: str
    stop_loss: float
    take_profit_1: float
    take_profit_2: float
    take_profit_3: float
    symbol: str = config('SYMBOL')
    timeframe: str = config('TIMEFRAME')
