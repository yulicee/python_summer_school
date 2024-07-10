def guest_book():
    names = []  
    
    while True:
        name = input("Enter your name (enter 'q' to quit): ").strip()
        if name.lower() == 'q':
            break  
        names.append(name)  
    
    filename = 'guest_book.txt'
    with open(filename, 'w+') as file:
        for name in names:
            file.write(name + '\n')
    
    print(f"Successfully wrote {len(names)} names to {filename}")

if __name__ == "__main__":
    guest_book()
