class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance tracking.
    """

    def __init__(self):
        """
        Initializes a Checkbook instance with a starting balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook.

        Parameters:
            amount (float): The amount to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook if sufficient funds are available.

        Parameters:
            amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance in the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Runs the interactive checkbook application,
    allowing the user to deposit, withdraw, check balance, or exit.
    """
    cb = Checkbook()

    while True:
        # Prompt user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            # Exit the program
            break

        elif action == 'deposit':
            # Handle deposit with input validation
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    cb.deposit(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the deposit.")

        elif action == 'withdraw':
            # Handle withdrawal with input validation
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    cb.withdraw(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the withdrawal.")

        elif action == 'balance':
            # Display the current balance
            cb.get_balance()

        else:
            # Handle unrecognized commands
            print("Invalid command. Please try again.")


# Run the main function if this script is executed
if __name__ == "__main__":
    main()
