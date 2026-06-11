from liquidity import detect_sweep
from mss import detect_mss
from score import calculate_score

highs = [100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,125]
lows = [90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110]

closes = [100,101,102,103,104,105]

sweep = detect_sweep(highs, lows)
mss = detect_mss(closes)

score = calculate_score(
    sweep=sweep,
    mss=mss
)

print("Sweep:", sweep)
print("MSS:", mss)
print("Score:", score)
