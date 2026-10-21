print("=" * 35)
print(" Road Trip Planner")
print("=" * 35)



# Ask their destination
destination = input("Where are you going on your road trip? ")
# Ask the total distance in miles for the road trip
miles_text = input("What is the total distance of your road trip in miles? ")
miles = float(miles_text)
# Ask how many days they will be traveling
days_text = input("How many days will you be traveling? ")
days = int(days_text)
# Ask their car's fuel efficiency in miles per gallon
mpg_text = input("What is your car's fuel efficiency (miles per gallon)? ")
mpg = float(mpg_text)
# Ask the current price of gas per gallon
gas_price_text = input("What is the current price of gas per gallon? $")
gas_price = float(gas_price_text)
# Ask the number of nights they will be staying
nights_text = input("How many nights will you be staying? ")
nights = int(nights_text)
# Ask the average cost of a hotel per night
hotel_cost_text = input("What is the average cost of a hotel per night? $")
hotel_cost = float(hotel_cost_text)
# Ask the average cost of food per day
food_cost_text = input("What is the average cost of food per day? $")
food_cost = float(food_cost_text)

# Calculate:
# Gallons of gas needed: distance / mpg
gallons = miles / mpg
# Total gas cost: gallons * gas_price
total_gas_cost = gallons * gas_price
# Total hotel cost: nights * hotel_cost
total_hotel_cost = nights * hotel_cost
# Total food cost: (nights + 1) * food_cost (one more day than nights)
total_food_cost = (nights + 1) * food_cost
# Grand total: sum of all costs
grand_total = total_gas_cost + total_hotel_cost + total_food_cost



print("=" * 35)
print("A brief summary of your road trip:")
print("=" * 35)



print(f"Your road trip to {destination} will take {days} days and cover {miles:.2f} miles.")
print(f"Your car will need {gallons:.2f} gallons of gas, which will cost ${total_gas_cost:.2f}.")
print(f"You will be staying for {nights} nights, which will cost ${total_hotel_cost:.2f}.")
print(f"You will be spending ${total_food_cost:.2f} on food for {nights + 1} days.")
print(f"The grand total for your road trip will be: ${grand_total:.2f}.")    



print("=" * 35)
print("Trip Summary")
print("=" * 35)



print(f"Destination: {destination}")
print(f"Days: {days}")
print(f"Total Miles: {miles:.2f}")
print(f"Gallons of Gas Needed: {gallons:.2f}")
print(f"Total Gas Cost: ${total_gas_cost:.2f}")
print(f"Total Hotel Cost: ${total_hotel_cost:.2f}")
print(f"Total Food Cost: ${total_food_cost:.2f}")
print(f"Grand Total: ${grand_total:.2f}")
print(f"Thank you for using the Road Trip Planner! Have a safe and enjoyable trip to {destination}!")



# Display a summary of the trip details and costs

# At the end, print a summary of the trip details and costs, including the destination, number of days, total miles, gallons of gas needed, total gas cost, total hotel cost, total food cost, and grand total.

#display a message thanking the user for using the road trip planner and wishing them a safe and enjoyable trip.