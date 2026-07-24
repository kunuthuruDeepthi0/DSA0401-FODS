import pandas as pd

# Read stock data from CSV file
data = pd.read_csv("stock_data.csv")

# Calculate variability
mean_price = data["Closing_Price"].mean()
std_dev = data["Closing_Price"].std()
minimum = data["Closing_Price"].min()
maximum = data["Closing_Price"].max()

print("Average Closing Price:", mean_price)
print("Standard Deviation:", std_dev)
print("Minimum Price:", minimum)
print("Maximum Price:", maximum)

# Provide insight
if std_dev > 10:
    print("Insight: Stock price shows high variability.")
else:
    print("Insight: Stock price shows relatively stable movement.")
