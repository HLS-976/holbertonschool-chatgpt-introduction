class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        else:
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_amount(prompt):
    while True:
        user_input = input(prompt)
        try:
            # Try to convert the input to a float
            amount = float(user_input)
            return amount
        except ValueError:
            # Handle invalid input
            print("Invalid input. Please enter a valid numeric value.")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            print("Exiting. Thank you for using the Checkbook!")
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
