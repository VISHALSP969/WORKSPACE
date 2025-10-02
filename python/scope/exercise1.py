# bank account balance tracker
balance=1000

def bank_account():
    balance=500

    def deposit(amount):
        nonlocal balance
        balance+=amount
        print(f"Deposited {amount}, New alance : {balance}")

    def withdraw(amount):
        nonlocal balance
        if amount<=balance:
            balance-=amount
            print(f"Withdrew {amount}, Remaining balance : {balance}")
        else:
            print("Insufficient funds!")
    
    deposit(200)
    withdraw(300)
    print("Final balance inside bank_accout:",balance)

bank_account()
print("Global balance is still",balance)