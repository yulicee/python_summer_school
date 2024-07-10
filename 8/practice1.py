import json

def store_favorite_number():
    favorite_number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    
    with open(filename, 'w+') as file:
        json.dump(favorite_number, file)
    
    print(f"Favorite number '{favorite_number}' has been stored in {filename}")

if __name__ == "__main__":
    store_favorite_number()
