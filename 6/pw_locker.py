import sys
import pyperclip

# Dictionary to store users and passwords
passwords = {
    'email': 'email_Pa$$w0rd',
    'facebook': 'facebook_Pa$$w0rd',
    'bank': 'bank_Pa$$w0rd'
}

MASTER_PASSWORD = 'master_Pa$$w0rd'

def main():
    # Ensure the program is run with the correct number of arguments
    if len(sys.argv) < 2:
        print('Usage: python password_locker.py [account] - copy account password')
        sys.exit(1)

    account = sys.argv[1]  # First command-line argument is the account name

    # Prompt for master password
    master_pass = input('Enter the master password: ')
    if master_pass != MASTER_PASSWORD:
        print('Invalid master password.')
    
    # Check if the account exists in the dictionary
    elif account in passwords:
        # Copy the password to the clipboard
        pyperclip.copy(passwords[account])
        print(f'Password for {account} copied to clipboard.')
        
        # For demonstration purposes, print the clipboard content
        clipboard_content = pyperclip.paste()
        print(f'Clipboard content: {clipboard_content}')
    else:
        print(f'There is no account named {account}.')

if __name__ == '__main__':
    main()
