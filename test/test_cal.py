from app.cal import add,subtract,multiply,divide,BankAccount
import pytest 
@pytest.fixture 
def zero_bank_Account():
    print("creating empty")
    return BankAccount() 
    
@pytest.fixture
def bank_account():
    return BankAccount(50)
@pytest.mark.parametrize("num1, num2 , expected",[(3,2,5),(7,1,8),(12,4,16)])

def test_add(num1,num2,expected):
    print("testing add function")
    assert add(num1,num2) == expected 

def test_sub():
    assert subtract(9,4) == 5 
 
def test_bank_set_amount():
    bank_account = BankAccount(50) 
    assert bank_account.balance == 50
def test_bank_default(zero_bank_Account):
    # bank_account = BankAccount() 
    print("testing my bank account")
    assert zero_bank_Account.balance == 0 
def test_withdraw():
    bank_account = BankAccount(100)
    bank_account.withdraw(50)
    assert bank_account.balance == 50 
def test_deposit():
    bank_account = BankAccount(100)
    bank_account.deposit(50)
    assert bank_account.balance == 150  
def test_collect_interest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round( bank_account.balance,6) == 55  

    


