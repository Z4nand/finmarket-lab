from finmarket_lab.market_data.bybit import BybitMarketData
from finmarket_lab.market_data.bybit import parse_orderbook
from finmarket_lab.visualization.orderbook_visualization import OrderbookView
from finmarket_lab.storage.writer import OrderbookWriter
import queue
import threading
import time
from IPython.display import clear_output, display as notebook_display

def viewer(display_queue):
    #Визуализация стакана
    orderbook_view = OrderbookView()
    while(True):
        bids, asks = parse_orderbook(display_queue.get())
        orderbook_view.display(bids,asks)
        time.sleep(0.1)

def saver(save_queue):
    #Сохрание данных стакана
    orderbook_writer = OrderbookWriter('../data/raw/BTCUSDT/orderbook_data.jsonl')
    while True:
        message = save_queue.get()
        orderbook_writer.save_message(message)

def main():
    display_queue = queue.Queue(maxsize=1)
    save_queue = queue.Queue()

    bmd = BybitMarketData(display_queue=display_queue, save_queue= save_queue)

    # Запустить в отдельном потоке, чтобы не блокировать
    receive_thread = threading.Thread(target=bmd.receive_orderbook, daemon=True)
    saver_thread = threading.Thread(target=saver, args= (save_queue,), daemon=True)

    receive_thread.start()
    saver_thread.start()

    viewer(display_queue=display_queue)

    
if __name__ =='__main__':
    main()