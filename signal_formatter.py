def create_signal(data):

    return f"""
🚀 {data['symbol']}

Liquidity: {data['sweep']}
MSS: {data['mss']}

Score: {data['score']}
"""
