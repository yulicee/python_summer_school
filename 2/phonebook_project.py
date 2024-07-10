# Get inputs
name = input("Enter Name: ")
address = input("Enter Address: ")
phone = input("Enter Phone Number: ")

# Format and display the information
print("\nFolgender Eintrag wurde gespeichert:")
print(f"Name:\t\t{name.upper()[:15] + '...'}")
print(f"Address:\t{address.upper()[:15] + '...'}")
print(f"Phone:\t\t{phone[:15] + '...'}")
