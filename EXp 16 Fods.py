from collections import Counter

with open("sample_text.txt", "r") as f:
    words = f.read().lower().split()

freq = Counter(words)

for word, count in freq.items():
    print(word, ":", count)
