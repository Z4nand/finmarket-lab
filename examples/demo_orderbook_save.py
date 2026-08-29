from finmarket_lab.market_data.bybit import BybitMarketData

bmd = BybitMarketData(depth =50)
bmd.receive_orderbook()

