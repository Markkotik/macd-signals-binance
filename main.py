from data.binance_spot import BinanceSpotDataSource

if __name__ == '__main__':
    cl = BinanceSpotDataSource()
    print(cl.connection_status())
    print(cl.get_data())