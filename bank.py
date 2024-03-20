class bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_widthraw=1000
        self.max_widthraw=1000000
        self.min_deposit=300
    
    def check_balance(self):
        print(f"Your current Balance {self.balance}")

    def deposit(self,amount):
        if amount < self.min_deposit:
            print(f"Cannot deposit {amount}")
        else:
            self.balance += amount
            print(f"Deposit Successfully Done.\nCurrent Balance: {self.balance}")

    
    def withdraw(self,amount):
        if amount < self.min_widthraw:
            print(f"amount is less than minimum withdraw, Cannot withdraw {amount} ")
        if amount > self.balance:
            print(f"Your Balance is {self.balance} you cannot withdraw {amount}")
        elif amount > self.max_widthraw:
            print(f"amount is greater than maximum withdraw Cannot withdraw {amount} ")
        else:
            self.balance -= amount
            print(f"Withdraw Successfully done.\nCurrent Balance: {self.balance}")


islamic=bank(50000)
islamic.check_balance()
islamic.withdraw(3000)
islamic.withdraw(3000)
islamic.withdraw(3000)
islamic.deposit(30000)

