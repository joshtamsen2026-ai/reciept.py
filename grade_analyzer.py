print("=" * 133)
print("---------------------------------------------------------- {Grade Analyzer} ---------------------------------------------------------")
print("=" * 133)

print("Welcome to your grade Analyzer, here you will be able to start with a list of the total scores for your class, see the classes average score, see the highest score, along with the lowest score. how many of those are passing and how many of those are failing. Along with those statistics you will receive a Grade distribution, be able to add more scores and get  an updated final average. ")


scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# Grade counters
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0

# Categorize grades using a for loop
for score in scores:
    if 90 <= score <= 100:
        a_count += 1
    elif 80 <= score <= 89:
        b_count += 1
    elif 70 <= score <= 79:
        c_count += 1
    elif 60 <= score <= 69:
        d_count += 1
    else:
        f_count += 1

# Calculate statistics
total_scores = len(scores)
average_score = sum(scores) / total_scores
highest_score = max(scores)
lowest_score = min(scores)

passing_count = 0
failing_count = 0

for score in scores:
    if score >= 60:
        passing_count += 1
    else:
        failing_count += 1

passing_percent = (passing_count / total_scores) * 100
failing_percent = (failing_count / total_scores) * 100

# Display results

print("=" * 133)


print("---------------------------------------------------------- Class Averages -----------------------------------------------------------")
print("=" * 133)


print(f"Total scores: {total_scores}")
print(f"Average: {average_score:.1f}")
print(f"Highest: {highest_score}")
print(f"Lowest: {lowest_score}")
print(f"Passing: {passing_count} ({passing_percent:.1f}%)")
print(f"Failing: {failing_count} ({failing_percent:.1f}%)")



print("Grade Distribution:")
print(f"A: {a_count} students")
print(f"B: {b_count} students")
print(f"C: {c_count} students")
print(f"D: {d_count} students")
print(f"F: {f_count} students")

# Add more scores using a while loop


print("=" *133)
print("---------------------------------------------------------- Add More Scores ----------------------------------------------------------")
print("=" *133)


while True:
    user_input = input("Enter a score (or 'done' to finish): ")

    if user_input.lower() == "done":
        break

    try:
        new_score = int(user_input)

        if 0 <= new_score <= 100:
            scores.append(new_score)
            updated_average = sum(scores) / len(scores)
            print(f"Updated average: {updated_average:.1f}")
        else:
            print("Please enter a score between 0 and 100.")

    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")


final_average = sum(scores) / len(scores)
print(f"\nFinal average: {final_average:.1f}")


print("Thank You for using our app today ! Hope you have a Wonderful rest of your day! ")