def generate_levels(price):

    entry = price

    sl = round(price * 0.99, 2)

    tp1 = round(price * 1.01, 2)
    tp2 = round(price * 1.02, 2)
    tp3 = round(price * 1.03, 2)

    return {
        "entry": entry,
        "sl": sl,
        "tp1": tp1,
        "tp2": tp2,
        "tp3": tp3
    }
