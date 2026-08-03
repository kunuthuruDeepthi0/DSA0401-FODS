from collections import Counter

reviews = [
    "Good product",
    "Very good quality",
    "Good service",
    "Excellent product"
]

words = " ".join(reviews).lower().split()
freq = Counter(words)

for word, count in freq.items():
    print(word, ":", count)
