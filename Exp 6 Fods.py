
prices = [50, 30, 20]       
quantities = [2, 3, 5]      
discount_rate = 10   
tax_rate = 5         

subtotal = sum(price * quantity for price, quantity in
               zip(prices, quantities))

discount = subtotal * (discount_rate / 100)

price_after_discount = subtotal - discount

tax = price_after_discount * (tax_rate / 100)

total_cost = price_after_discount + tax


print("Subtotal:", subtotal)
print("Discount:", discount)
print("Tax:", tax)
print("Total Cost:", total_cost)
