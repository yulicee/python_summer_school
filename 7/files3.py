filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object.read().splitlines():
        print(line)

print(" ")
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.read().splitlines()

for line in lines:
    print(line)

print(" ")
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object.read().splitlines():
        modified_line = line.lower().replace('you', 'dogs').strip()
        print(modified_line)
