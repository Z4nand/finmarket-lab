from finmarket_lab.market_data.bybit import BybitMarketData

bmd = BybitMarketData(queue='заглушка')
bmd.receive_orderbook()