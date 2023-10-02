from dataclasses import dataclass

from decouple import config


@dataclass
class Signal:
    time: str
    indicator_name: str
    direction: str
    symbol: str = config('SYMBOL')
    timeframe: str = config('TIMEFRAME')
