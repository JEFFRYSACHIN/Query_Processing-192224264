import pandas as pd

import matplotlib.pyplot as plt

data = {
    "Date": pd.date_range(start="2023-01-01", periods=10, freq="D"),
    "Stock Price": [150, 152, 153, 155, 157, 156, 158, 160, 162, 165],
    "Trading Volume": [1000, 1100, 1050, 1200, 1250, 1300, 1400, 1350, 1450, 1500]
}

df = pd.DataFrame(data)

# Line Plot
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Stock Price"], label="Stock Price")
plt.title("Stock Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()
