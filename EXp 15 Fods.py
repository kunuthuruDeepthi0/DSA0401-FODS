import pandas as pd

# Read temperature data from CSV file
data = pd.read_csv("temperature_data.csv")

# Group data city-wise
city_data = data.groupby("City")["Temperature"]

# 1. Calculate mean temperature for each city
mean_temp = city_data.mean()

# 2. Calculate standard deviation for each city
std_temp = city_data.std()

# 3. Calculate temperature range for each city
temp_range = city_data.max() - city_data.min()

print("Mean Temperature:")
print(mean_temp)

print("\nStandard Deviation:")
print(std_temp)

print("\nCity with Highest Temperature Range:")
print(temp_range.idxmax(), "=", temp_range.max())

print("\nMost Consistent City:")
print(std_temp.idxmin(), "with standard deviation =", std_temp.min())
