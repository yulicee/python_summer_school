# Initialize an empty list
numbers = []

# Prompt user to input 10 numbers and add them to the list
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Print list
print("\nOriginal list")
print(*numbers, sep=", ")

# Remove first and last numbers from the list
numbers.pop(0)
numbers.pop(-1)

# Print list after removal
print("\nList after removing first and last numbers: ")
print(*numbers, sep=", ")

# Find and print the max and min numbers in the list
max_num = max(numbers)
min_num = min(numbers)
print("\nMaximum number:")
print(max_num)
print("Minimum number:")
print(min_num)

# Calculate and print the sum and average of the numbers
total_sum = sum(numbers)
average = total_sum // len(numbers)  # Integer division for average
print("\nSum of the numbers:")
print(total_sum)
print("Average of the numbers:")
print(average)

# Sort and print the list in ascending order
numbers.sort()
print("\nList in ascending order:")
print(*numbers, sep=", ")

# Sort and print the list in descending order
numbers.sort(reverse=True)
print("\nList in descending order:")
print(*numbers, sep=", ")
