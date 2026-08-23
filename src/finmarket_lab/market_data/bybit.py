from time import sleep
from pybit.unified_trading import WebSocket

def handle_message(message: dict)->None:
        print(message)

def save_message(message: dict):
    message = str(message)
    with open('example.txt','w',encoding='utf-8') as f:
        f.write(message)
    
class BybitMarketData:
    def connect(self):  
        pass
    
   
    
    def receive_orderbook(self):
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
    
    def save(self,data):
        pass