from finmarket_lab.market_data.bybit import BybitMarketData
import queue
import threading
import time

data_queue = queue.Queue()
bmd = BybitMarketData(queue=data_queue)

# Запустить в отдельном потоке, чтобы не блокировать
thread = threading.Thread(target=bmd.receive_orderbook, daemon=True)
thread.start()

# Подождать немного и посмотреть очередь
time.sleep(3)
print(len(data_queue.queue))

