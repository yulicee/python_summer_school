# Initialize two lists with at least 5 words each
list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry']
list2 = ['banana', 'date', 'fig', 'grape', 'apple']

# Convert the lists to sets to remove any duplicate words
set1 = set(list1)
set2 = set(list2)

# Print original sets of words
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Find and print the union of the two sets
union_set = set1.union(set2)
print(f"Union: {union_set}")

# Find and print the intersection of the two sets
intersection_set = set1.intersection(set2)
print(f"Intersection: {intersection_set}")

# Find and print the difference between the first set and the second set
difference_set1 = set1.difference(set2)
print(f"Difference (Set1 - Set2): {difference_set1}")

# Find and print the difference between the second set and the first set
difference_set2 = set2.difference(set1)
print(f"Difference (Set 2 - Set 1): {difference_set2}")