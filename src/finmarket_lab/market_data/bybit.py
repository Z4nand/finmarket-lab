from time import sleep
from pybit.unified_trading import WebSocket
import os
import json
import queue

    
class BybitMarketData:
    def __init__(
            self, 
            queue,
            symbol="BTCUSDT", 
            depth=50, 
            testnet=False,
            path=None,):
        self.queue = queue
        self.symbol = symbol
        self.depth = depth
        self.testnet = testnet
        
        if path is None:
            self.path = f'data/raw/{self.symbol}/orderbook_data.jsonl'
        else:
            self.path = path
        
        # Создаем папки, если их нет
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
            
        self.ws=WebSocket(
            testnet=self.testnet,
            channel_type= "linear",
        )
    
    def _print_message(self, message: dict):
        print(message)
        
    def _save_message(self, message: dict):
        try:
            with open(self.path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(message) + '\n')
        except Exception as e:
            print(f'Error: {e}')
            
    def _callback(self,message: dict)->None:
        if message:
            self.queue.put(message)
        
   
    
    def receive_orderbook(self):
       
        self.ws.orderbook_stream(
            depth = self.depth,
            symbol = self.symbol,
            callback = self._callback,
        )
        while True:
            sleep(1)
    
        
  