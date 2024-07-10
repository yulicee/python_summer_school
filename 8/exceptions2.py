def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"Contents of {filename}:")
            print(contents)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

def main():
    read_file('cats.txt')
    read_file('dogs.txt')
    read_file('rabbits.txt')  

if __name__ == "__main__":
    main()
