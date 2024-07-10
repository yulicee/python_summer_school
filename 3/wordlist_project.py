# Empty list
words = []

# User input prompt
for i in range(10):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

# Print list
print("\nOriginal list: ")
print(*words, sep=", ")

# Remove a word specified by user from list
while True:
    word_to_remove = input("\nEnter a word to remove from the list: ")
    if word_to_remove in words:
        words.remove(word_to_remove)
        break
    else:
        print(f"The word '{word_to_remove}' is not in the list. Choose a word from the list you provided.")

# Print list after removal
print("\nList after removal: ")
print(*words, sep=", ")

# Find and print the longest and shortest words in the list
longest_word = max(words, key=len)
shortest_word = min(words, key=len)
print("\nLongest word: ")
print(longest_word)
print("\nShortest word: ")
print(shortest_word)

# Count and print the occurences of each word
print("\nOccurrences of each word: ")
word_counts = {word: words.count(word) for word in set (words)}
for word, count in word_counts.items():
    print(f"{word}: {count}")

# Sort and print list alphabetically
words.sort()
print("\nList in alphabetical order: ")
print(*words, sep=", ")

# Print list in reverse alphabetical order
words.sort(reverse=True)
print("\nList in reverse alphabetical order: ")
print(*words, sep=", ")