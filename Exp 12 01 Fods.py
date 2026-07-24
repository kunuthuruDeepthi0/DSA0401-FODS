import matplotlib.pyplot as plt

# Monthly data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [22, 24, 28, 32, 35, 34, 33, 32, 31, 29, 26, 23]

# Create line plot
plt.plot(months, temperature, marker='o', color='blue', linewidth=2)

# Add title and labels
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")

# Display grid
plt.grid(True)

# Show the plot
plt.show()
