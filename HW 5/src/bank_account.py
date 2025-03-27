"""
File: bank_account.py
Author: Karina Solis
Date: 3/10/25
Resources:
    - Wolf Paulus: Python Syntax, BankAccount Outline, midterm.py
"""
import functools
import json

# Decorators (from Midterm)
def log_transaction(func:callable):
    """Logs any transaction that changes the account balance"""
    @functools.wraps(func)
    def wrapper(self, amount:float):
        result = func(self, amount)
        self.transactions.append(f"{func.__name__}: ${amount}")
        return result
    return wrapper

def validate_amount(func:callable):
    """ This decorator will make sure that the amount is positive and that the account has the sufficient balance"""
    @functools.wraps(func)
    def wrapper(self, amount:float):
        if (amount < 0):
            raise ValueError(f"Cannot {func.__name__} negative amount.")
        elif (amount == 0):
            raise ValueError(f"Cannot {func.__name__} 0")
        elif (func.__name__ == "withdraw"):
            if (amount > self.balance):
                raise ValueError(f"Cannot withdraw {amount}. Insufficient funds. Balance: ${self.balance}")
        return func(self, amount)
    return wrapper

# Bank Account Class
class BankAccount:
    """A simple BankAccount class with methods to deposit, withdraw, and get_balance."""
    
    def __init__(self, account_number=0, owner="", balance=0):
        """Initialize a BankAccount with an owner and an optional starting balance."""
        self.account_number = account_number
        self.owner = owner
        self.transactions = []
        if (balance < 0):
            raise ValueError("Cannot Initialize Account with negative balance.")
        self.balance = balance

    def from_json(self, filename:str) -> dict | None:
        """Deserialize a BankAccount object from a json file."""
        with open(filename, "r") as file:
            data = json.load(file)
            file.close()
        self.account_number = data["account_number"]
        self.owner = data["owner"]
        self.balance = int(data["balance"])
        self.transactions = data["transactions"]

    def to_json(self, filename:str):
        """Serialize a BankAccount object to a json file."""
        with open(filename, "w") as file:
            file.write(json.dumps(self.__dict__))
            file.close()

    @validate_amount
    @log_transaction
    def deposit(self, amount:float):
        """Deposit a positive amount to the account."""
        self.balance += amount

    @validate_amount
    @log_transaction
    def withdraw(self, amount:float):
        """Withdraw a positive amount if sufficient balance exists."""
        self.balance -= amount
        
    def get_balance(self):
        """Return the current balance."""
        return self.balance
        
    def show_transactions(self):
        """Prints all account transactions."""
        for transaction in self.transactions:
            print(f"{transaction}")