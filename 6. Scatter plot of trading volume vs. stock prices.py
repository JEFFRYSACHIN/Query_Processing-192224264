import pandas as pd

import matplotlib.pyplot as plt

data = {
    "Date": pd.date_range(start="2023-01-01", periods=10, freq="D"),
    "Stock Price": [150, 152, 153, 155, 157, 156, 158, 160, 162, 165],
    "Trading Volume": [1000, 1100, 1050, 1200, 1250, 1300, 1400, 1350, 1450, 1500]
}

df = pd.DataFrame(data)

# Scatter Plot
plt.figure(figsize=(10, 5))
plt.scatter(df["Trading Volume"], df["Stock Price"], c="green")
plt.title("Volume vs Price")
plt.xlabel("Trading Volume")
plt.ylabel("Stock Price")
plt.show()
