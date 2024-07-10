class SWIFT:
    @classmethod
    def iban(cls, country_code, bank_code, account_number):
        country_code = cls.landeskuerzel(country_code)
        bank_code = cls.bankleitzahl(bank_code)
        account_number = cls.kontonummer(account_number)
        bban = cls.bban(bank_code, account_number)
        check_digits = cls.pruefzahl(country_code, bban)
        iban = f"{country_code}{check_digits}{bban}"
        return iban

    @staticmethod
    def landeskuerzel(country_code):
        return country_code.upper()

    @staticmethod
    def bankleitzahl(bank_code):
        # Ensure bank code does not have leading zeros
        bank_code_str = str(bank_code)
        if len(bank_code_str) != 8:
            raise ValueError("Bank code should be exactly 8 digits.")
        if bank_code_str[0] == '0':
            raise ValueError("Bank code should not have a leading zero.")
        return bank_code_str

    @staticmethod
    def kontonummer(account_number):
        account_number_str = str(account_number)
        if len(account_number_str) > 10:
            raise ValueError("Account number should not exceed 10 digits.")
        if all(char == '0' for char in account_number_str):
            raise ValueError("Account number cannot consist of only zeros.")
        return f"{account_number:010d}"

    @staticmethod
    def bban(bank_code, account_number):
        return bank_code + account_number

    @staticmethod
    def zahlFuerUpper(character):
        if character.isupper() and len(character) == 1:
            return ord(character) - ord('A') + 10
        else:
            raise ValueError("Input must be a single uppercase letter")

    @staticmethod
    def bbanErgaenzung(country_code):
        return f"{SWIFT.zahlFuerUpper(country_code[0])}{SWIFT.zahlFuerUpper(country_code[1])}00"

    @classmethod
    def zahlAlsStringMod97(cls, digits):
        remainder = int(digits) % 97
        return remainder

    @classmethod
    def pruefzahl(cls, country_code, bban):
        extended_bban = bban + cls.bbanErgaenzung(country_code)
        remainder = cls.zahlAlsStringMod97(extended_bban)
        check_digits = 98 - remainder
        return f"{check_digits:02d}"

def main():
    # Example usage with user input
    country_code = input("Enter the country code (e.g., DE): ").strip().upper()
    
    # Input and validate bank code (BLZ)
    while True:
        bank_code_input = input("Enter the bank code (BLZ) as an 8-digit number: ").strip()
        try:
            bank_code = int(bank_code_input)
            if len(bank_code_input) != 8:
                raise ValueError("Bank code should be exactly 8 digits.")
            if bank_code < 0 or bank_code > 99999999:
                raise ValueError("Bank code should be between 00000000 and 99999999.")
            if bank_code_input[0] == '0':
                raise ValueError("Bank code should not have a leading zero.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Input and validate account number
    while True:
        account_number_input = input("Enter the account number as a max 10-digit number: ").strip()
        try:
            account_number = int(account_number_input)
            if len(account_number_input) > 10:
                raise ValueError("Account number should not exceed 10 digits.")
            if account_number < 0 or account_number > 9999999999:
                raise ValueError("Account number should be between 0000000000 and 9999999999.")
            account_number_str = str(account_number)
            if all(char == '0' for char in account_number_str):
                raise ValueError("Account number cannot consist of only zeros.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    # Generate IBAN and display
    try:
        iban = SWIFT.iban(country_code, bank_code, account_number)
        print(f"\nGenerated IBAN: {iban}")
    except ValueError as e:
        print(f"Error generating IBAN: {e}")

if __name__ == "__main__":
    main()
