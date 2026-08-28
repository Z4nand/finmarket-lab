#from src.finmarket_lab.storage.reader import ReaderDataOrderbook
#from src.finmarket_lab.visualization.visualization import v1_barhs


# rdo = ReaderDataOrderbook()
# df= rdo.read_csv('data/raw/example.csv')

from finmarket_lab.market_data.bybit import BybitMarketData
bmd = BybitMarketData(depth =50)
bmd.receive_orderbook()

