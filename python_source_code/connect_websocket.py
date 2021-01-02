from config import *
import websocket
import json

SOCKET_ENDPOINT = "wss://data.alpaca.markets/stream"
STOCKS = ["Q.AAPL"]
# T. is trades (ie all trades executed by exchanges)  Q. is quotes (what people are willing to buy/sell for)

# all websockets take 3 mandatory functions: on open, on message, and on close.
# On open gets called once when we try to connect
# on message gets called each time we get a new piece of data sent to us
# on close gets called when we close the connection (stop listening to data)


def on_open(ws):
    # we have to send an authentication message
    auth_data = {
        "action": "authenticate",
        "data": {
            "key_id": f"{KEY}",
            "secret_key": f"{SECRET_KEY}"
        }
    }
    # authenticate our connection
    ws.send(json.dumps(auth_data))

    channel_data = {
        "action": "listen",
        "data": {"streams": STOCKS}  # streams is what channels we want to subscribe to
    }

    ws.send(json.dumps(channel_data))


def on_message(ws, message):
    # every time a message gets sent to us we have to define what to do.  In this instance we'll just print it
    # but we can get more complex by doing stuff like analyzing the high frequency data to make orders
    print("received a message")
    print(message)


def on_close(ws):
    print("closed connection")


ws = websocket.WebSocketApp(SOCKET_ENDPOINT, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()

