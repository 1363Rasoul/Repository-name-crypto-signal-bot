import requests

def get_klines(symbol, interval="5m", limit=200):

    url = "https://api.binance.com/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params)

    return response.json()
