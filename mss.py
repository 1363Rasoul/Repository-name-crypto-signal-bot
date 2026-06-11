def detect_mss(closes):

    if closes[-1] > max(closes[-5:-1]):
        return "bullish"

    if closes[-1] < min(closes[-5:-1]):
        return "bearish"

    return None
