import pandas as pd
order_data = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102, 101],
    'order_date': ['2026-07-01', '2026-07-02', '2026-07-05',
                   '2026-07-03', '2026-07-06', '2026-07-08'],
    'product_name': ['Laptop', 'Mouse', 'Laptop',
                     'Keyboard', 'Mouse', 'Keyboard'],
    'order_quantity': [1, 2, 1, 3, 1, 2]
})

order_data['order_date'] = pd.to_datetime(order_data['order_date'])
orders_per_customer = order_data.groupby('customer_id').size()
avg_quantity = order_data.groupby('product_name')['order_quantity'].mean()

earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()


print("Order Data:")
print(order_data)

print("\n1. Total Orders by Each Customer:")
print(orders_per_customer)

print("\n2. Average Order Quantity for Each Product:")
print(avg_quantity)

print("\n3. Earliest Order Date:", earliest_date.date())
print("Latest Order Date:", latest_date.date())
