import json

def read_favorite_number():
    filename = 'favorite_number.json'
    
    try:
        with open(filename, 'r+') as file:
            favorite_number = json.load(file)
            print(f"I know your favorite number! It's {favorite_number}.")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please run the first program to store your favorite number.")

if __name__ == "__main__":
    read_favorite_number()
