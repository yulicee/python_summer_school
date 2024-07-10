filename = 'learning_python.txt'

# Read the file and replace 'Python' with 'C'
with open(filename, 'r+') as file:
    for line in file:
        modified_line = line.lower().replace('you', 'dogs').strip()
        print(modified_line.strip())
