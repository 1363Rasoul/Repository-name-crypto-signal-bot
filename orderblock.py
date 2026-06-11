def detect_orderblock(candles):

    if len(candles) < 5:
        return None

    last_candle = candles[-2]

    if last_candle["close"] < last_candle["open"]:
        return "bullish_ob"

    if last_candle["close"] > last_candle["open"]:
        return "bearish_ob"

    return None
