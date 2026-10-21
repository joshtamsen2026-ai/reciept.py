#Robust Number Collector

# Ask the user to input 3 numbers one at a time

#Wraps each input() + int() conversion in a try/except ValueError

def collect_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Collect 3 numbers from the user
numbers = []
for i in range(3):
    numbers.append(collect_number(f"Enter number {i + 1}: "))
    
#After all 3 inputs, prints:
#Each number entered
#The sum
#The average (as a float with 2 decimal places)
print("\nResults:")
for i, number in enumerate(numbers, start=1):
    print(f"Number {i}: {number}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")

