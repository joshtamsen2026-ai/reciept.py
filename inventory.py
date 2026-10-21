#Start with a dictionary of at least 4 products. Each product should have a name (key) with a nested dictionary containing price (float) and quantity (int):
from operator import add


inventory = {
    "laptop": {"price": 999.99, "quantity": 10},
    "mouse": {"price": 29.99, "quantity": 50},
    "keyboard": {"price": 79.99, "quantity": 30},
    "monitor": {"price": 199.99, "quantity": 20}
}   
#Display the full inventory in a formatted table
print("Inventory:")
print("-" * 50)
for product, details in inventory.items():
    print(f"{product.capitalize()}:")
    print(f"  Price: ${details['price']:.2f}")
    print(f"  Quantity: {details['quantity']}")
print("-" * 50)

#Calculate and display the total value of the inventory (price × quantity for each product, summed)
total_value = sum(details['price'] * details['quantity'] for details in inventory.values())
print(f"Total Inventory Value: ${total_value:.2f}")

#Let the user look up a product and see its details (using .get() for safety)
search_product = input("Enter the name of the product to look up: ").lower()
product_details = inventory.get(search_product)

if product_details:
    print(f"Product: {search_product.capitalize()}")
    print(f"Price: ${product_details['price']:.2f}")
    print(f"Quantity: {product_details['quantity']}")
else:
    print(f"Product '{search_product}' not found.")

#Let the user update the quantity of a product (simulating a sale or restock)
update_product = input("Enter the name of the product to update: ").lower()
if update_product in inventory:
    new_quantity = int(input("Enter the new quantity: "))
    inventory[update_product]['quantity'] = new_quantity
    print(f"Quantity for '{update_product}' updated to {new_quantity}.")
else:
    print(f"Product '{update_product}' not found.")

#Use a set to track which products are "low stock" (quantity < 10)
low_stock_products = {product for product, details in inventory.items() if details['quantity'] < 50}
print(f"Low Stock Products: {low_stock_products}")

#add Display the full inventory in a formatted table
print("Inventory:")
print("-" * 50)
for product, details in inventory.items():
    print(f"{product.capitalize()}:")
    print(f"  Price: ${details['price']:.2f}")
    print(f"  Quantity: {details['quantity']}")
    

#allow user to add a new product to the inventory (with name, price, and quantity)

add_product = input("Would you like to add a new product? (yes/no): ").strip().lower()
if add_product == "yes":
    new_product_name = input("Enter the name of the new product: ").lower()
    new_product_price = float(input("Enter the price of the new product: "))
    new_product_quantity = int(input("Enter the quantity of the new product: "))
    inventory[new_product_name] = {"price": new_product_price, "quantity": new_product_quantity}
    print(f"Product '{new_product_name}' added to inventory.")  
    print("Updated Inventory:")
    print("-" * 50)
    for product, details in inventory.items():
        print(f"{product.capitalize()}:")
        print(f"  Price: ${details['price']:.2f}")
        print(f"  Quantity: {details['quantity']}")
        print("formatted table")
        #add a low stock alert for any product that has a quantity less than 5
        if details['quantity'] < 5:
            print(f"  ALERT: '{product.capitalize()}' is low on stock!")    


