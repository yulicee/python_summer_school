class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("\nInsufficient funds. Transaction cancelled")
    
    def display(self):
        print(f"\nOwner: {self.owner}, Balance: ${self.balance:.2f}")

def main():
    print("Welcome to the Simple Bank Account.\n")

    owner = input("Enter the owner's name: ")
    initial_balance = float(input("Initial balance: "))
    account = BankAccount(owner, initial_balance)

    while True:
        print("\nChoose an option: ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display balance")
        print("4. Exit")
              
        option = input("\nOptions: ")

        if option == '1':
            amount = float(input("Enter amount to deposit: $"))
            account.deposit(amount)
        elif option == '2':
            amount = float(input("Enter amount to withdraw: $"))
            account.withdraw(amount)
        elif option == '3':
            account.display()
        elif option == '4':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Please choose again.")

if __name__ == "__main__":
    main()