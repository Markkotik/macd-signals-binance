import pandas as pd


class MacdSignal:

    def __init__(self):
        self.data = None

    def add_macd_lines(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Add MACD and Signal lines to the dataframe.

        :param data: The dataframe with TOHLC data.
        :return: The dataframe with added MACD and Signal lines.
        """
        df = data.copy()
        df['ma_fast'] = df['C'].ewm(span=12, adjust=False).mean()
        df['ma_slow'] = df['C'].ewm(span=26, adjust=False).mean()
        df['macd'] = df['ma_fast'] - df['ma_slow']
        df['signal'] = df['macd'].ewm(span=9, adjust=False).mean()
        self.data = df
        return df

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

    def detect(self, data: pd.DataFrame) -> str:
        """
        Detects MACD crossover signals within the given data.

        :param data: The data in which to detect the signal.
        :return: 'buy' if a MACD crossover buy signal is detected,
                 'sell' if a MACD crossover sell signal is detected,
                 'none' otherwise.
        """
        self.add_macd_lines(data)
        if self.is_buy_signal():
            return 'buy'
        elif self.is_sell_signal():
            return 'sell'
        else:
            return 'none'
