import random
import string

class Account:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        self.account_number = self._generate_account_number()

    def _generate_account_number(self):
        return ''.join(random.choices(string.digits, k=10))

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount
        print(f"{self.name} deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"{self.name} withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def transfer(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)
        print(f"{self.name} transferred ${amount:.2f} to {other_account.name}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"{self.name} | Account: {self.account_number} | Balance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, initial_deposit=0.0):
        account = Account(name, initial_deposit)
        self.accounts.append(account)
        print(f"Created account for {name} with initial deposit ${initial_deposit:.2f}")
        return account

    def get_account_by_name(self, name):
        for acc in self.accounts:
            if acc.name == name:
                return acc
        return None

    def print_all_accounts(self):
        print("\n--- All Bank Accounts ---")
        for acc in self.accounts:
            print(acc)


def simulate_bank_operations():
    bank = Bank()
    alice = bank.create_account("Alice", 500)
    bob = bank.create_account("Bob", 300)

    alice.deposit(150)
    bob.withdraw(50)
    alice.transfer(bob, 100)

    print("\nFinal balances:")
    print(alice)
    print(bob)

    bank.print_all_accounts()


if __name__ == "__main__":
    simulate_bank_operations()
