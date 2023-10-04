from decouple import config


def timeframe_to_seconds(timeframe: str = config('TIMEFRAME')) -> int:
    """
    Convert a timeframe string to its equivalent in seconds.

    Args:
    - timeframe (str): The timeframe string. Examples include '1m', '1h', '1d', etc.

    Returns:
    - int: The number of seconds the timeframe represents.

    Raises:
    - ValueError: If the timeframe string is not recognized.
    """

    multiplier = int(timeframe[:-1])

    unit = timeframe[-1]

    match unit:
        case 's':
            return multiplier
        case 'm':
            return multiplier * 60
        case 'h':
            return multiplier * 60 * 60
        case 'd':
            return multiplier * 60 * 60 * 24
        case 'w':
            return multiplier * 60 * 60 * 24 * 7
        case 'M':
            # Note: Using a month as a time interval can be imprecise as months can have a variable number of days.
            # Here, we assume a month has 30 days.
            return multiplier * 60 * 60 * 24 * 30
        case _:
            raise ValueError(f"Unknown timeframe: {timeframe}")
