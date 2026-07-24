import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 170, 200, 220]

# Create bar plot
plt.bar(months, sales, color='green')

# Labels and title
plt.title("Monthly Sales Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales")

# Show plot
plt.show()
