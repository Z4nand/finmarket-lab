import matplotlib.pyplot as plt
import numpy as np

# Пример данных стакана
bids_prices = np.array([100.5, 100.4, 100.3, 100.2, 100.1])
bids_volumes = np.array([10, 25, 50, 80, 120])  # Кумулятивный объем или объем на уровне

asks_prices = np.array([100.6, 100.7, 100.8, 100.9, 101.0])
asks_volumes = np.array([15, 30, 45, 90, 150])

fig, ax = plt.subplots(figsize=(8, 5))

# Горизонтальные бары: Покупки (Bids) зеленые слева/справа, Продажи (Asks) красные
ax.barh(bids_prices, bids_volumes, color='green', alpha=0.6, height=0.08, label='Bids')
ax.barh(asks_prices, asks_volumes, color='red', alpha=0.6, height=0.08, label='Asks')

ax.set_title('Биржевой стакан (Order Book)')
ax.set_xlabel('Объем')
ax.set_ylabel('Цена')
ax.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()
