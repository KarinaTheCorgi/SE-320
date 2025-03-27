"""
File: test_bank_account.py
Author: Karina Solis
Date: 3/10/25
Resources:
    - Wolf Paulus: Python Syntax
    - Parameterization
        - https://docs.pytest.org/en/latest/example/parametrize.html
        - https://docs.pytest.org/en/latest/reference/reference.html#pytest.raises
        - https://docs.pytest.org/en/latest/how-to/fixtures.html#fixture-parametrize-marks
"""

import pytest
from bank_account import BankAccount

@pytest.fixture
def starting_balance():
    return 0

@pytest.fixture
def bank_account(starting_balance):
    return BankAccount(12345, "Karina", starting_balance)

# JSON Deserialization and Serialization Tests
def test_to_json(bank_account):
    bank_account.to_json('example.json')
    
def test_from_json(bank_account):
    bank_account2 = BankAccount()
    bank_account2.from_json('example2.json')
    assert bank_account2.balance == 123
    assert bank_account2.account_number == 56789
    assert bank_account2.owner == "Test-Owner"

# Deposit Tests
def test_deposit(bank_account):
    """ Test should pass if deposit method runs correctly """
    bank_account.deposit(100)
    assert bank_account.balance == 100

def test_deposit_negative_amount(bank_account):
    """ Test should raise ValueError for negative deposit """
    with pytest.raises(ValueError):
        bank_account.deposit(-100)

# Withdraw Test
@pytest.mark.parametrize("starting_balance", [100])
def test_withdraw(bank_account):
    """ Test should pass if withdraw method runs correctly  """
    bank_account.withdraw(70)
    assert bank_account.balance == 30
    
@pytest.mark.parametrize("starting_balance", [250])
def test_withdraw_too_much(bank_account):
    """ Test should raise ValueError for withdrawing more than balance """
    with pytest.raises(ValueError):
        bank_account.withdraw(300)
    
def test_withdraw_negative_amount(bank_account):
    """ Test should raise ValueError for negative withdraw """
    with pytest.raises(ValueError):
        bank_account.withdraw(-50)

# Get Balance Test    
def test_get_balance(bank_account):
    """ Test should pass if get_balance method runs correctly  """
    bank_account.balance = 12345
    assert bank_account.get_balance() == 12345
    
# Edge Case Tests
def test_withdraw_zero(bank_account):
    """ Test should catch withdrawing 0  """
    with pytest.raises(ValueError):
        bank_account.withdraw(0)

def test_deposit_zero(bank_account):
    """ Test should catch depositing 0  """
    with pytest.raises(ValueError):
        bank_account.withdraw(0)
        
def test_negative_init():
    with pytest.raises(ValueError):
        BankAccount(12345, "Karina", -200)