import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, MaxNLocator
from IPython.display import display as notebook_display

class OrderbookView:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(9, 6))
        self.fig.subplots_adjust(left=0.18, right=0.96, bottom=0.12, top=0.9)
        self.price_limits = None
        self.volume_limit = 0
        self.display_handle = None

    def display(self, bids, asks):
        if not bids or not asks:
            return
        # Очищение полотна перед отрисовкой новых графиков, чтоб не наслаивались
        self.ax.clear()
        
        #Разбиение на price и value
        prices_bids = [price for price, volume in bids]
        volumes_bids = [volume for price, volume in bids]
        prices_asks = [price for price, volume in asks]
        volumes_asks = [volume for price, volume in asks]

        prices = sorted(set(prices_bids + prices_asks))
        price_step = min((b - a for a, b in zip(prices, prices[1:])), default=0.1)
        bar_height = price_step * 0.8
        low, high = prices[0] - price_step, prices[-1] + price_step

        # Масштаб сохраняется между кадрами; меняется только при выходе за границы.
        if self.price_limits is None or low < self.price_limits[0] or high > self.price_limits[1]:
            span = high - low
            if self.price_limits is not None:
                span = max(span, (self.price_limits[1] - self.price_limits[0]) / 1.4)
            center = (low + high) / 2
            self.price_limits = (center - span * 0.7, center + span * 0.7)
        max_volume = max(volumes_bids + volumes_asks)
        if max_volume > self.volume_limit:
            self.volume_limit = max_volume * 1.25

        self.ax.barh(
            y = prices_bids,
            width = volumes_bids,
            height = bar_height,
            color = '#16a085',
            label = 'Покупки'
        )
        self.ax.barh(
            y = prices_asks,
            width = volumes_asks,
            height = bar_height,
            color = '#e76676',
            label = 'Продажи'
        )
        
        self.ax.set_xlabel("Объём")
        self.ax.set_ylabel("Цена")
        self.ax.set_title("Стакан BTCUSDT")
        self.ax.set_xlim(0, self.volume_limit or 1)
        self.ax.set_ylim(*self.price_limits)
        self.ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.2f}'))
        self.ax.yaxis.set_major_locator(MaxNLocator(nbins=10))
        self.ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
        self.ax.set_facecolor('#f6f8fa')
        self.ax.set_axisbelow(True)
        self.ax.grid(axis='x', color='#dce2e8', linewidth=0.7)
        self.ax.spines[['top', 'right']].set_visible(False)
        self.ax.legend(loc='upper right', framealpha=0.9)

        # plt.show()
        if self.display_handle is None:
            self.display_handle = notebook_display(self.fig, display_id=True)
        else:
            self.display_handle.update(self.fig)
        plt.close(self.fig)
