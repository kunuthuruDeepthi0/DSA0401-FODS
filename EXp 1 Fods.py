import numpy as np

student_scores = np.array([
    [85, 78, 92, 88],
    [90, 82, 85, 91],
    [76, 89, 80, 84],
    [88, 91, 87, 90]
])

subjects = ["Math", "Science", "English", "History"]

average_scores = np.mean(student_scores, axis=0)

print("Average Scores:")
for i in range(len(subjects)):
    print(subjects[i], ":", average_scores[i])

highest_avg_index = np.argmax(average_scores)

print("\nSubject with Highest Average Score:", subjects[highest_avg_index])
print("Highest Average Score:", average_scores[highest_avg_index])
