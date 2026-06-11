from binance_client import get_klines
from liquidity import detect_sweep
from mss import detect_mss
from score import calculate_score

def analyze(symbol="BTCUSDT"):

    candles = get_klines(symbol)

    highs = [float(c[2]) for c in candles]
    lows = [float(c[3]) for c in candles]
    closes = [float(c[4]) for c in candles]

    sweep = detect_sweep(highs, lows)
    mss = detect_mss(closes)

    score = calculate_score(
        sweep=sweep,
        mss=mss
    )

    return {
        "symbol": symbol,
        "sweep": sweep,
        "mss": mss,
        "score": score
    }
