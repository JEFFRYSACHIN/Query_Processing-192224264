import pandas as pd
import numpy as np

# Create a DataFrame with 10 rows and 4 columns of random values
np.random.seed(42)
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Highlight negative and positive numbers manually
def format_dataframe(row):
    return [f'\033[91m{val:.2f}\033[0m' if val < 0 else f'\033[90m{val:.2f}\033[0m' for val in row]

# Print the formatted DataFrame
for index, row in df.iterrows():
    print(format_dataframe(row))
