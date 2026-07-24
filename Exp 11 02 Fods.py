import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 170, 200, 220]

# Create scatter plot
plt.scatter(months, sales, color='red', s=100)

# Labels and title
plt.title("Monthly Sales Scatter Plot")
plt.xlabel("Months")
plt.ylabel("Sales")

# Show plot
plt.show()
