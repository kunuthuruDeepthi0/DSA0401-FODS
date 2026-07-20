import numpy as np
fuel_efficiency = np.array([25, 30, 35, 40])
average_efficiency = np.mean(fuel_efficiency)
percentage_improvement = ((fuel_efficiency[3] - fuel_efficiency[0])
                          / fuel_efficiency[0]) * 100


print("Fuel Efficiency (MPG):", fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency, "MPG")
print("Percentage Improvement:", percentage_improvement, "%")
