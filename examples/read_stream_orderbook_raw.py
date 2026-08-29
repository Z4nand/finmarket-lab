from finmarket_lab.storage.reader import ReaderDataOrderbook

rdo = ReaderDataOrderbook('data/raw/BTCUSDT/orderbook_data.jsonl')
out = rdo.read_stream()
print(type(out))