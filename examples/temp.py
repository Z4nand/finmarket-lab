import pandas as pd
import numpy as np

bids_prices = np.array([100.5, 100.4, 100.3, 100.2, 100.1])
bids_volumes = np.array([10, 25, 50, 80, 120])

asks_prices = np.array([100.6, 100.7, 100.8, 100.9, 101.0])
asks_volumes = np.array([15, 30, 45, 90, 150])

# Создаем DataFrame
df = pd.DataFrame({
    'side': ['bid'] * len(bids_prices) + ['ask'] * len(asks_prices),
    'price': np.concatenate([bids_prices, asks_prices]),
    'volume': np.concatenate([bids_volumes, asks_volumes])
})

# Сохраняем в CSV
df.to_csv('example.csv', index=False)