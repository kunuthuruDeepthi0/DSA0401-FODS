import matplotlib.pyplot as plt

# Monthly data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

rainfall = [15, 20, 30, 45, 80, 120, 150, 140, 100, 60, 35, 20]

# Create scatter plot
plt.scatter(months, rainfall, color='green', s=100)

# Add title and labels
plt.title("Monthly Rainfall")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")

# Display grid
plt.grid(True)

# Show the plot
plt.show()
