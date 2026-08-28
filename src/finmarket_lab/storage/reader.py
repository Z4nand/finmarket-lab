import pandas as pd

class ReaderDataOrderbook:
    
    def __init__(self, a=0):
        self.a = a
    
    def read(self,path: str)->str:
        temp = ''
        with open(path, 'r', encoding='utf-8') as f:
            temp = f.read()  #TODO переделать на построчную загрузку
        return temp
    
    def read_csv(self, path: str):
        temp = pd.read_csv(path)
        return temp
            