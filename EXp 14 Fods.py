import pandas as pd
import matplotlib.pyplot as plt

# Create student data
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Exam_Score": [45, 50, 55, 60, 65, 70, 75, 80, 88, 92]
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df["Study_Hours"].corr(df["Exam_Score"])

print("Correlation coefficient:", correlation)

if correlation > 0:
    print("There is a positive correlation between study time and exam scores.")
elif correlation < 0:
    print("There is a negative correlation between study time and exam scores.")
else:
    print("There is no correlation.")

# Scatter plot
plt.scatter(df["Study_Hours"], df["Exam_Score"])
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.title("Study Time vs Exam Score")
plt.grid(True)
plt.show()
