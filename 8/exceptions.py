def main():
    invalid_input_count = 0
    
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            
            break  # Exit the input loop if valid numbers are entered

        except ValueError:
            invalid_input_count += 1
            print("Error: Invalid input. Please enter a valid number.")

            if invalid_input_count >= 2:
                choice = input("Do you want to continue despite errors? (yes/no, default yes): ").strip().lower()
                if choice != 'yes':
                    print("Exiting the program due to repeated errors. Goodbye!")
                    return

    while True:
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")

        choice = input("Do you want to continue? (yes/no, default yes): ").strip().lower()
        if choice != 'yes':
            break

        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

    choice = input("Do you want to start over? (yes/no, default no): ").strip().lower()
    if choice != 'yes':
        print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
