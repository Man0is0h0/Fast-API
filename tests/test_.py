import pytest
from app.utils import add,BankAccount,InsufficientFunds


@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, ans",[
    (3,2,5),
    (7,1,8),
    (12,4,16)
])
def test_add(num1,num2,ans):
    print("testing add function")
    assert add(num1,num2)==ans 

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance==0

def test_bank_set_initial_ammount():
    bank_account=BankAccount(50)
    assert bank_account.balance==50

def test_bank_deposit():
    bank_account=BankAccount()
    initial_balance=bank_account.balance
    bank_account.deposit(100)
    assert bank_account.balance-initial_balance==100

def test_bank_withdraw():
    bank_account=BankAccount(200)
    initial_balance=bank_account.balance
    bank_account.withdraw(100)
    assert initial_balance-bank_account.balance==100

def test_collect_interest():
    bank_account=BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance,0)==55


@pytest.mark.parametrize("deposited,credited,ans",[
    (300,200,100),
    (50,10,40),
    (1200,200,1000)
])
def test_bank_transactions(zero_bank_account,deposited,credited,ans):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(credited)
    assert zero_bank_account.balance==ans

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
