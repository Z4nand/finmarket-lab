import pandas as pd
import json

class OrderbookReader:
    
    def __init__(
            self, 
            filepath):
        self.filepath = filepath
    
    def read_all(self):
        messages = []
        with open(self.filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    messages.append(json.loads(line))
        return messages
    
    def read_stream(self):
        with open(self.filepath, 'r',encoding='utf-8') as f:
            return f.readlines()[-1]
        
    def read_csv(self, path: str):
        temp = pd.read_csv(path)
        return temp
            