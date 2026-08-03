import pandas as pd

df = pd.DataFrame({
    "Age": [22, 25, 22, 30, 25, 22, 28, 30]
})

print(df["Age"].value_counts().sort_index())
