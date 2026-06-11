def detect_sweep(highs, lows):

    recent_high = max(highs[-20:-1])
    recent_low = min(lows[-20:-1])

    if highs[-1] > recent_high:
        return "BSL"

    if lows[-1] < recent_low:
        return "SSL"

    return None
