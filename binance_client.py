import requests

def get_klines(symbol="BTCUSDT", interval="15m", limit=100):

    url = "https://api.binance.com/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params)

    return response.json()
