import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 170, 200, 220]

# Create line plot
plt.plot(months, sales, marker='o', color='blue', linewidth=2)

# Labels and title
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")

# Display grid
plt.grid(True)

# Show plot
plt.show()
