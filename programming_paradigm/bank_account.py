# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        Default balance is 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit the given amount to the account.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the given amount from the account.
        If there are sufficient funds, deduct and return True.
        Else, return False.
        """
        if amount > self.account_balance:
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
