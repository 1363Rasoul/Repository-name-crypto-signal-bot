def calculate_score(
    sweep,
    mss
):

    score = 0

    if sweep:
        score += 40

    if mss:
        score += 40

    return score
