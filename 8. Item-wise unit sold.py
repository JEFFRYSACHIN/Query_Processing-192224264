import pandas as pd
data = {
    "OrderDate": pd.date_range(start="2018-01-01", periods=10, freq="M"),
    "Region": ["East", "Central", "Central", "Central", "West", "East", "Central", "West", "East", "Central"],
    "Manager": ["Martha", "Hermann", "Hermann", "Timothy", "Timothy", "Martha", "Hermann", "Douglas", "Martha", "Hermann"],
    "SalesMan": ["Alexander", "Shelli", "Luis", "David", "Stephen", "Alexander", "Steven", "Michael", "Alexander", "Sigal"],
    "Item": ["Television", "Home Theater", "Television", "Cell Phone", "Television", "Home Theater", "Television", "Television", "Home Theater", "Home Theater"],
    "Units": [95, 50, 36, 27, 56, 60, 75, 32, 60, 90],
    "Unit_price": [1198, 500, 1198, 225, 1198, 500, 1198, 1198, 500, 1198],
    "Sale_amt": [113810, 25000, 43128, 6075, 67088, 30000, 89850, 38336, 30000, 107820]
}

df = pd.DataFrame(data)

# Item wise unit sold
pivot_units = pd.pivot_table(df, values="Units", index="Item", aggfunc="sum")
print(pivot_units)
