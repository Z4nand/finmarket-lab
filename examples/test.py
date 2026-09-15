from finmarket_lab.market_data.bybit import parse_orderbook 
from finmarket_lab.storage.reader import OrderbookReader
from finmarket_lab.visualization.orderbook_visualization import OrderbookView

rdo = OrderbookReader('data/raw/BTCUSDT/orderbook_data.jsonl')
out = rdo.read_all()

message = out[0]
bids, asks = parse_orderbook(message)

orderbook_view = OrderbookView()
orderbook_view.display(bids, asks)