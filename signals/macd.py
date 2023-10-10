from abc import abstractmethod
from datetime import datetime
from typing import Union

import pandas as pd

from models.signal_model import Signal
from decouple import config


class MacdSignal(Signal):

    def __init__(self):
        self.data = None

    @abstractmethod
    def identify_signal(self, data: pd.DataFrame) -> Union[Signal, None]:
        """
        Detects MACD crossover signals within the provided data.

        :param data: Data in which to detect the signal.
        :return: Signal object containing timestamp, indicator name, direction, entry price,
                 stop loss, and three take-profit levels.
        """
        self.add_macd_lines(data)

        if self.is_buy_signal():
            direction = 'buy'
        elif self.is_sell_signal():
            direction = 'sell'
        else:
            return None

        time = datetime.now().isoformat()

        levels = self.calculate_levels(direction)

        return Signal(time=time,
                      indicator_name="MACD",
                      direction=direction,
                      entry_price=levels["entry_price"],
                      stop_loss=levels["stop_loss"],
                      take_profit_1=levels["take_profit_1"],
                      take_profit_2=levels["take_profit_2"],
                      take_profit_3=levels["take_profit_3"])

    def calculate_levels(self, direction: str) -> dict:
        """
        Calculate stop loss and take profits based on given direction and current entry price.

        Args:
        - direction (str): Either 'buy' or 'sell'.

        Returns:
        - dict: A dictionary containing entry price, stop loss and take profit levels.
        """

        entry_price = float(self.data['C'].iloc[-1])

        stop_loss_percent = self._get_config_percentage("STOP_LOSS_PERCENT")
        take_profit_percents = [
            self._get_config_percentage("TAKE_PROFIT_1_PERCENT"),
            self._get_config_percentage("TAKE_PROFIT_2_PERCENT"),
            self._get_config_percentage("TAKE_PROFIT_3_PERCENT")
        ]

        if direction == 'buy':
            stop_loss = self._adjusted_price(entry_price, stop_loss_percent, False)
            take_profits = [self._adjusted_price(entry_price, tp, True) for tp in take_profit_percents]
        elif direction == 'sell':
            stop_loss = self._adjusted_price(entry_price, stop_loss_percent, True)
            take_profits = [self._adjusted_price(entry_price, tp, False) for tp in take_profit_percents]
        else:
            raise ValueError(f"Unexpected direction value: {direction}")

        round_decimal_places = int(config('ROUND_DECIMAL_PLACES'))

        return {
            "stop_loss": round(stop_loss, round_decimal_places),
            "entry_price": entry_price,
            "take_profit_1": round(take_profits[0], round_decimal_places),
            "take_profit_2": round(take_profits[1], round_decimal_places),
            "take_profit_3": round(take_profits[2], round_decimal_places),
        }

    @staticmethod
    def _get_config_percentage(key: str) -> float:
        """
        Retrieve the configuration value for a given key and convert it to percentage.
        """
        return float(config(key)) / 100

    @staticmethod
    def _adjusted_price(price: float, percentage: float, increase: bool) -> float:
        """
        Adjust the given price by a certain percentage.
        """
        factor = 1 + percentage if increase else 1 - percentage
        return price * factor

    def add_macd_lines(self, data: pd.DataFrame):
        """
        Add MACD and Signal lines to the dataframe.

        :param data: The dataframe with TOHLC data.
        :return: The dataframe with added MACD and Signal lines.
        """
        df = data
        df['ma_fast'] = df['C'].ewm(span=12, adjust=False).mean()
        df['ma_slow'] = df['C'].ewm(span=26, adjust=False).mean()
        df['macd'] = df['ma_fast'] - df['ma_slow']
        df['signal'] = df['macd'].ewm(span=9, adjust=False).mean()
        self.data = df

    def is_buy_signal(self) -> bool:
        """
        Check if a MACD crossover buy signal is present in the last two candles.

        :return: True if a MACD crossover buy signal is detected, False otherwise.
        """
        latest_macd_above_signal = self.data['macd'].iloc[-1] > self.data['signal'].iloc[-1]
        previous_macd_below_signal = self.data['macd'].iloc[-2] < self.data['signal'].iloc[-2]

        return latest_macd_above_signal and previous_macd_below_signal

    def is_sell_signal(self) -> bool:
        """
        Check if a MACD crossover sell signal is present in the last two candles.

        :return: True if a MACD crossover sell signal is detected, False otherwise.
        """
        latest_macd_below_signal = self.data['macd'].iloc[-1] < self.data['signal'].iloc[-1]
        previous_macd_above_signal = self.data['macd'].iloc[-2] > self.data['signal'].iloc[-2]

        return latest_macd_below_signal and previous_macd_above_signal
