import pandas as pd

df = pd.DataFrame({
    "Likes": [100, 150, 100, 200, 150, 100, 250, 200]
})

print(df["Likes"].value_counts().sort_index())
