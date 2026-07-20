import numpy as np

# House data
# Columns: Bedrooms, Square_Feet, Sale_Price
house_data = np.array([
    [3, 1500, 300000],
    [5, 2500, 500000],
    [4, 1800, 350000],
    [6, 3200, 700000],
    [5, 2700, 600000]
])

# Find houses with more than 4 bedrooms
houses = house_data[house_data[:, 0] > 4]

# Calculate average sale price
average_price = np.mean(houses[:, 2])

print("House Data:")
print(house_data)

print("\nAverage Sale Price of Houses with More Than 4 Bedrooms =", average_price)
