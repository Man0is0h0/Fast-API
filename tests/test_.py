import pytest
from app.utils import add,BankAccount

@pytest.mark.parametrize("num1, num2, ans",[
    (3,2,5),
    (7,1,8),
    (12,4,16)
])
def test_add(num1,num2,ans):
    print("testing add function")
    assert add(num1,num2)==ans 

def test_bank_set_initial_ammount():
    bank_account=BankAccount(50)
    assert bank_account.balance==50

def test_bank_deposit():
    bank_account=BankAccount()
    initial_balance=bank_account.balance
    bank_account.deposit(100)
    assert bank_account.balance-initial_balance==100

def test_bank_withdraw():
    bank_account=BankAccount()
    initial_balance=bank_account.balance
    bank_account.withdraw(100)
    assert initial_balance-bank_account.balance==100

def test_collect_interest():
    bank_account=BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance,0)==55