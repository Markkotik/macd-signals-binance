import time

from data.binance_spot import BinanceSpotDataSource
from notifications.telegram import TelegramNotifier
from signals.macd import MacdSignal
from visualisations.macd_visualizer import MACDVisualization

if __name__ == '__main__':

    cl = BinanceSpotDataSource()
    macd_signal = MacdSignal()
    messenger = TelegramNotifier()

    print('Bot started')

    while True:
        df = cl.get_data()
        signal = macd_signal.identify_signal(df)

        if signal.direction != 'none':
            visualization = MACDVisualization()
            image_path = visualization.visualize(df, signal)
            messenger.send(signal, image_path)

            print(signal)

        time.sleep(60)
