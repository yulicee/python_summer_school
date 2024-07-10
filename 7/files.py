filename = 'learning_python.txt'

print("Reading the entire file at once:")
with open(filename, 'r+') as file:
    content = file.read()
    print(content)

print("\nReading line by line:")
with open(filename, 'r+') as file:
    for line in file:
        print(line.strip())

