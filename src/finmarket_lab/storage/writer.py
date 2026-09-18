import os
import json

class OrderbookWriter:
    def __init__(
            self,
            path=None,):

        self.path = path
        
        # Создаем папки, если их нет
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def save_message(self, message: dict):
        try:
            with open(self.path, 'a', encoding='utf-8') as f:
                f.write(json.dumps(message) + '\n')
        except Exception as e:
            print(f'Error: {e}')    
            