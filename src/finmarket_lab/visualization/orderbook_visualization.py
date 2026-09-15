import matplotlib.pyplot as plt

class OrderbookView:
    def __init__(self):
        pass

    def display(self, bids, asks):
        fig, ax = plt.subplots()

        #Разбиение на price и value
        prices_bids = [price for price, volume in bids]
        volumes_bids = [volume for price, volume in bids]
        prices_asks = [price for price, volume in asks]
        volumes_asks = [volume for price, volume in asks]

        ax.barh(
            y = prices_bids,
            width = volumes_bids,
            height = 0.2,
            color = 'green',
            label = 'bids'
        )
        ax.barh(
            y = prices_asks,
            width = volumes_asks,
            height = 0.2,
            color = 'red',
            label = 'asks'
        )
        
        ax.set_xlabel = ("Объём")
        ax.set_ylabel = ("Цена")
        ax.set_title  = ("Стакан BTCUSDT")
        ax.legend()

        plt.show()
