from passlib.context import CryptContext
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash_password(password:str):
    return pwd_context.hash(password)

def verify(plain_pass,hashed_pass):
    return pwd_context.verify(plain_pass,hashed_pass)

def add(a:int,b:int):
    return a+b

class InsufficientFunds(Exception):
    pass

class BankAccount():
    def __init__(self,starting_balance=0):
        self.balance=starting_balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientFunds("Insufficient funds in account")
        self.balance-=amount
    def collect_interest(self):
        self.balance*=1.1