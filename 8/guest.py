def guest():
    name = input("Please enter your name: ")

    filename = 'guest.txt'
    with open(filename, 'w+') as file:
        file.write(name)
    
    print(f"You successfully wrote '{name}' to {filename}")

if __name__ == "__main__":
    guest()
