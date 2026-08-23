from time import sleep
from pybit.unified_trading import WebSocket

def handle_message(message: dict)->None:
    print(message)

ws = WebSocket(
    testnet = False,
    channel_type= "linear",
)

ws.orderbook_stream(
    depth = 50,
    symbol = "BTCUSDT",
    callback = handle_message,
)

while True:
    sleep(1)