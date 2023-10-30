class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number =  account_number #public attribute
        self.balance =  balance #public attribute
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insuffictent balance.")
    def get_balance(self):
        return self.balance
#Create an instance of the BankAccount class
account = BankAccount("1234567890",1000)
#Accessing the private attribute directly
#Error: AttributeError: 'BankAccount' object has no attribute '__balance'
print("Current balance:",account.balance)

#We need to access the private attributes using get method
print("Current balance:",account.get_balance())
#Depositing and withdrawing funds
account.deposit(500)
account.withdraw(200)

#Checking the updated balance
print("Current balance:",account.get_balance())