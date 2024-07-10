def convert_base(number: int, base_input: str) -> str:
    base_input = base_input.strip().upper()
    
    if base_input.isdigit():
        base = int(base_input)
        if base < 2 or base > 16:
            raise ValueError("Invalid base. Supported bases are 2 to 16.")
    else:
        base = int(base_input, 16)
    
    if number == 0:
        return "0"

    digits = "0123456789ABCDEF"
    result = ""
    current_number = abs(number)

    while current_number > 0:
        remainder = current_number % base
        result = digits[remainder] + result
        current_number //= base

    if number < 0:
        result = '-' + result

    return result

while True:
    print("\nWelcome to the Base Conversion Utility\n")
    
    try:
        # Input number in base 10
        number = int(input("Enter the number: "))
    
        # Input the base to convert to
        base_input = input("Enter the base to convert to: ").strip()
    
        converted_number = convert_base(number, base_input)
        print(f"The number {number} from base 10 to base {base_input} is {converted_number}\n")
    
    except ValueError as e:
        print(f"Error: {e}\n")
    
    # Ask if the user wants to perform another conversion
    another_conversion = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
    if another_conversion != 'yes':
        print("Goodbye!")
        break
