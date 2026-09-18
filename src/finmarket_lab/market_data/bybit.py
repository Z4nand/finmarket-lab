from time import sleep
from pybit.unified_trading import WebSocket
import os
import queue

def parse_orderbook(message):
    bids = [
        [float(price), float(volume)]
        for price, volume in message["data"]["b"]
    ]

    asks = [
        [float(price), float(volume)]
        for price, volume in message["data"]["a"]
    ]

    return bids, asks
    
class BybitMarketData:
    def __init__(
            self, 
            display_queue,
            save_queue,
            symbol="BTCUSDT", 
            depth=50, 
            testnet=False,
            path=None,):
        self.display_queue = display_queue
        self.save_queue = save_queue 
        self.symbol = symbol
        self.depth = depth
        self.testnet = testnet
        
        self.ws=WebSocket(
            testnet=self.testnet,
            channel_type= "linear",
        )
    
    def _print_message(self, message: dict):
        print(message)

    def _display_queue_put(self, message):
        try:
            self.display_queue.put_nowait(message)
        except queue.Full:
            # Убираем устаревшее сообщение.
            try:
                self.display_queue.get_nowait()
            except queue.Empty:
                # Визуализация уже успела его забрать.
                pass

            self.display_queue.put_nowait(message)

            
    def callback(self,message: dict)->None:
        if message:
            self.save_queue.put_nowait(message)
            self._display_queue_put(message)


    def receive_orderbook(self):
       
        self.ws.orderbook_stream(
            depth = self.depth,
            symbol = self.symbol,
            callback = self.callback,
        )
        while True:
            sleep(1)
    