import pandas as pd

# Create DataFrame
sales_data = pd.DataFrame({
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse',
                     'Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Monitor'],
    'quantity_sold': [5, 10, 7, 8, 6, 4, 9, 5, 3, 2]
})

# Find the top 5 products sold the most
top5_products = sales_data.groupby('product_name')['quantity_sold'].sum() \
                          .sort_values(ascending=False) \
                          .head(5)

print("Top 5 Products Sold:")
print(top5_products)
