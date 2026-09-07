from finmarket_lab.storage.reader import ReaderDataOrderbook

rdo = ReaderDataOrderbook('data/raw/BTCUSDT/orderbook_data.jsonl')
out = rdo.read_all()

print(out[0])