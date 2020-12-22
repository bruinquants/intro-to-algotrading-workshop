import requests
import json
import pandas as pd
from config import *

# go to https://alpaca.markets/docs/api-documentation/api-v2 to see API documentation.

# trading API endpoints
ACCOUNT_URL = f"{BASE_URL}/v2/account"
ORDER_URL = f"{BASE_URL}/v2/orders"
POSITIONS_URL = f"{BASE_URL}/v2/positions"
ASSETS_URL = f"{BASE_URL}/v2/assets"


# endpoint for historical is different from our trading API
HISTORICAL_URL = f"https://data.alpaca.markets"


def get_account():
    # get our account information - cash, value invested, ect.
    r = requests.get(url=ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)


def get_positions():
    # returns our portfolio - set of all our positions (ie what we have bought)
    r = requests.get(url=POSITIONS_URL, headers=HEADERS)
    return json.loads(r.content)


def make_order(symbol: str, qty: int, side: str, order_type: str, time_in_force: str, limit_price: float):

    # check out the orders documentation to see in depth what these mean.
    # Type, time in force, and limit price can definitely be a bit confusing
    data = {
        "symbol": symbol,
        "qty": qty,  # number of shares
        "side": side,  # buy or sell
        "type": order_type,  # will usually be market or limit
        "time_in_force": time_in_force,  # usually gtc(good till cancelled) or ioc(immediate or cancel). Lookup for more
        "limit_price": limit_price  # required if our type is limit. This is the maximum price we're willing to pay
    }
    r = requests.post(url=ORDER_URL, json=data, headers=HEADERS)
    return json.loads(r.content)


def get_orders():
    # returns orders that have not yet become positions
    r = requests.get(url=ORDER_URL, headers=HEADERS)
    return json.loads(r.content)


def get_order(symbol: str):
    url = f"{ORDER_URL}/{symbol}"
    r = requests.get(url=url, headers=HEADERS)
    return json.loads(r.content)


def delete_orders():
    # attempt to close all open orders (i.e. haven't been filled), returns 500 if order is no longer cancellable

    # we might want to do this for various reasons: say we have lots of orders we placed in after hours that won't be
    # filled until the start of the next trading day.  If the market gets bad then we might want to cancel the orders
    r = requests.delete(url=ORDER_URL, headers=HEADERS)
    return json.loads(r.content)


def delete_position(symbol: str, qty=None):
    # will liquidate our stake in the position
    if qty is None:
        qty = get_positions()[symbol]["qty"]  # unless specified, sell all shares
    url = f"{POSITIONS_URL}/{symbol}"
    data = {"qty": qty}
    r = requests.delete(url=url, json=data, headers=HEADERS)
    return json.loads(r.content)


def get_historical_data(timeframe: str, symbols: str, limit: int, start: str, end: str):
    # timeframe is our frequency, one of: minute, 1min, 5min, 15min, day, 1D
    # gets data for our symbols between start and end.  If we include multiple, separate by commas
    # limit is the max number of instances we want to show in the response

    url = f"{HISTORICAL_URL}/v1/bars/{timeframe}?symbols={symbols}&limit={limit}&start={start}&end={end}"
    r = requests.get(url=url, headers=HEADERS)
    return json.loads(r.content)


def make_dataframe(json_data, asset):
    return pd.DataFrame.from_dict(json_data[asset])


if __name__ == "__main__":
    acc = get_account()
    print(acc)
    pos = get_positions()
    print(pos)
    test = make_order("AAPL", 1, "buy", "market", "day", None)
    # None is because we don't specify limit price for market order.  Limit price is a requirement to order
    # at that price or better, whereas for a market order we'll take whatever we can get


    # visit https://app.alpaca.markets/paper/dashboard/overview to see your order
    print(test)

    historical = get_historical_data("day", "AAPL", 100, '2020-01-01', '2020-12-12')
    # schema for historical response is at
    # https://alpaca.markets/docs/api-documentation/api-v2/market-data/bars/#bars-entity
    print(historical)
    print(make_dataframe(historical, "AAPL"))
