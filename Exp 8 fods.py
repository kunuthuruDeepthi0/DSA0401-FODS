import pandas as pd

# Create DataFrame
property_data = pd.DataFrame({
    'property_id': [101, 102, 103, 104, 105],
    'location': ['Hyderabad', 'Chennai', 'Hyderabad', 'Bangalore', 'Chennai'],
    'bedrooms': [3, 5, 4, 6, 2],
    'area_sqft': [1500, 2500, 1800, 3200, 1200],
    'listing_price': [5000000, 8000000, 6000000, 12000000, 4500000]
})

# 1. Average listing price in each location
avg_price = property_data.groupby('location')['listing_price'].mean()

# 2. Number of properties with more than four bedrooms
more_than_4 = property_data[property_data['bedrooms'] > 4].shape[0]

# 3. Property with the largest area
largest_property = property_data.loc[property_data['area_sqft'].idxmax()]

# Display Results
print("Property Data:")
print(property_data)

print("\n1. Average Listing Price by Location:")
print(avg_price)

print("\n2. Number of Properties with More Than 4 Bedrooms:")
print(more_than_4)

print("\n3. Property with the Largest Area:")
print(largest_property)
