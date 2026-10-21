item1_name = "Notebook"
item1_price = "4.99"
item1_quantity = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_quantity = "1"
tax_rate = "0.075"


# 7.5% sales tax

item1_price_float = float(item1_price)
item1_quantity_int = int(item1_quantity)        
item2_price_float = float(item2_price)
item2_quantity_int = int(item2_quantity)    
tax_rate_float = float(tax_rate)

item1_subtotal = item1_price_float * item1_quantity_int
item2_subtotal = item2_price_float * item2_quantity_int
total_subtotal = item1_subtotal + item2_subtotal
tax_amount = total_subtotal * tax_rate_float
total_amount = total_subtotal + tax_amount

print(f"Item 1: {item1_name}")
print(f"Price: ${item1_price_float:.2f}")
print(f"Quantity: {item1_quantity_int}")
print(f"Subtotal: ${item1_subtotal:.2f}")
print(f"Item 2: {item2_name}")
print(f"Price: ${item2_price_float:.2f}")
print(f"Quantity: {item2_quantity_int}")
print(f"Subtotal: ${item2_subtotal:.2f}")
print(f"Total Subtotal: ${total_subtotal:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Total Amount: ${total_amount:.2f}")
