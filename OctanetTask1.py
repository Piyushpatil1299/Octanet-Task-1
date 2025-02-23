# ATM Machine Simulation in Python

class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def authenticate(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            print("Authentication successful!\n")
            return True
        else:
            print("Incorrect PIN. Access denied.\n")
            return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
        self.transaction_history.append("Balance inquiry")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${self.balance}")
            self.transaction_history.append(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount}. New balance: ${self.balance}")
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Invalid amount or insufficient funds.")

    def change_pin(self):
        new_pin = input("Enter your new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("PIN changed")
        else:
            print("Invalid PIN format. PIN must be a 4-digit number.")

    def show_transaction_history(self):
        print("\nTransaction History:")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(f"- {transaction}")
        else:
            print("No transactions yet.")

# Main function to run the ATM simulation
def run_atm():
    atm = ATM(pin="1234", balance=1000)  # Initialize with a default PIN and balance

    if atm.authenticate():
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Cash")
            print("3. Withdraw Cash")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Select an option (1-6): ")

            if choice == '1':
                atm.check_balance()
            elif choice == '2':
                atm.deposit()
            elif choice == '3':
                atm.withdraw()
            elif choice == '4':
                atm.change_pin()
            elif choice == '5':
                atm.show_transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid selection. Please choose a valid option.")

# Run the ATM program
if __name__ == "__main__":
    run_atm()
