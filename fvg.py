def detect_fvg(highs, lows):

    for i in range(1, len(highs)-1):

        if lows[i+1] > highs[i-1]:
            return "bullish"

        if highs[i+1] < lows[i-1]:
            return "bearish"

    return None
