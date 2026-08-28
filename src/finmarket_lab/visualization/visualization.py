import matplotlib.pyplot as plt
import numpy as np
from ..storage.reader import ReaderDataOrderbook

rdo = ReaderDataOrderbook()
df= rdo.read_csv('data/raw/example.csv')
print(df)

def v1_barhs(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    # Горизонтальные бары: Покупки (Bids) зеленые слева/справа, Продажи (Asks) красные
    ax.barh(df['side']=='bid', df['volume'], color='green', alpha=0.6, height=0.08, label='Bids')
    ax.barh(df['side']=='ask', df['volume'], color='red', alpha=0.6, height=0.08, label='Asks')

    ax.set_title('Биржевой стакан (Order Book)')
    ax.set_xlabel('Объем')
    ax.set_ylabel('Цена')
    ax.legend()
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.show()