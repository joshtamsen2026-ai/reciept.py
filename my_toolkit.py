
print("Side note i did try to understand to the best of my ability the assignments requirements and had to use pylance(as i had a decent amount of redlines to fix in the small viewer at the top right of the screen) in order to correct a lot of lines of code but i hope this is what you were looking for in regards to the practice assignment")



"""

#This is my_toolkit.py homework/practicework


#A collection of utility functions for working with lists,
strings, and score reports.
"""


def calculate_average(numbers):
    """
#Calculate and return the average of a list of numbers.

#Returns 0 if the list is empty.
    """
    if len(numbers) == 0:
        return 0

    total = 0
    for number in numbers:
        total += number

    return total / len(numbers)


def find_max_and_min(numbers):
    """
#Find and return the maximum and minimum values in a list.

#Does not use the built-in max() or min() functions.
#Returns None if the list is empty.
    """
    if len(numbers) == 0:
        return None

    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number

        if number < min_value:
            min_value = number

    return (max_value, min_value)


def count_occurrences(items, target):
    """
#Count and return the number of times a target value
appears in a list.

#Does not use the built-in .count() method.
    """
    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


def is_palindrome(text):
    """
#Return True if the text reads the same forward
and backward.

#Comparison is case-insensitive and ignores spaces.
    """
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]


def create_report(title, scores):
    """
#Create and return a formatted report containing
summary information about a list of scores.

#Uses calculate_average() and find_max_and_min()
internally.
    """
    average = calculate_average(scores)
    max_min = find_max_and_min(scores)

    if max_min is None:
        max_score = "N/A"
        min_score = "N/A"
    else:
        max_score, min_score = max_min

    report = (
        f"===== {title} =====",
        f"Number of Scores: {len(scores)}",
        f"Average Score: {average:.2f}",
        f"Highest Score: {max_score}",
        f"Lowest Score: {min_score}",)

    return report


if __name__ == "__main__":
# Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]

print(f"Average: {calculate_average(test_scores)}")
print(f"Max/Min: {find_max_and_min(test_scores)}")
print(f"Count of 85: {count_occurrences(test_scores, 85)}")
print(f"'racecar' palindrome: {is_palindrome('racecar')}")
print(f"'hello' palindrome: {is_palindrome('hello')}")
print()
print(create_report("Class Scores", test_scores))

print("=" * 40)
print("EDGE CASE TESTS")
print("=" * 40)

# Empty list tests
print("Empty List Tests")
empty_list = []
print(f"Average of empty list: {calculate_average(empty_list)}")
print(f"Max/Min of empty list: {find_max_and_min(empty_list)}")

# Multiple occurrence tests
print("Count Occurrence Tests")
repeated_items = [1, 2, 2, 3, 2, 4, 2]
print(f"Occurrences of 2: {count_occurrences(repeated_items, 2)}")
print(f"Occurrences of 99: {count_occurrences(repeated_items, 99)}")

# Palindrome edge cases
print("Palindrome Tests")
print(f"'A man a plan a canal Panama': {is_palindrome('A man a plan a canal Panama')}")
print(f"'Madam': {is_palindrome('Madam')}")
print(f"'x': {is_palindrome('x')}")
print(f"Empty string: {is_palindrome('')}")
print(f"'Never odd or even': {is_palindrome('Never odd or even')}")

# Single-item list tests
print("Single Item List Tests")
single_item = [42]
print(f"Average: {calculate_average(single_item)}")
print(f"Max/Min: {find_max_and_min(single_item)}")

# Negative number tests
print("Negative Number Tests")
negative_numbers = [-10, -5, -20, -1]
print(f"Average: {calculate_average(negative_numbers)}")
print(f"Max/Min: {find_max_and_min(negative_numbers)}")

# Empty report test
print("Empty Report Test")
print(create_report("Empty Scores", []))