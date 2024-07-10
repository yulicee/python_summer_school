def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.islower():
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt_message(message, shift):
    decrypted_message = ""
    for char in message:
        if char.islower():
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        elif char.isupper():
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message

while True:
    print("\nWelcome to the Easy Caesar Cipher!")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ").strip()
    
    if choice == '1':
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        encrypted_msg = encrypt_message(message, shift)
        print(f"Encrypted message: {encrypted_msg}")
        
    elif choice == '2':
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        decrypted_msg = decrypt_message(message, shift)
        print(f"Decrypted message: {decrypted_msg}")
        
    elif choice == '3':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please choose from the menu (1-3).")

