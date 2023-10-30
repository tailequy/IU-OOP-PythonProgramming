class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number =  account_number # private attribute
        self.__balance =  balance #private attribute
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insuffictent balance.")
    def get_balance(self):
        return self.__balance
#Create an instance of the BankAccount class
account = BankAccount("1234567890",1000)
#Accessing the private attribute directly
#Error: AttributeError: 'BankAccount' object has no attribute '__balance'
#print("Current balance:",account.__balance)

#We need to access the private attributes using get method
print("Current balance:",account.get_balance())
#Depositing and withdrawing funds
account.deposit(500)
account.withdraw(200)

#Checking the updated balance
print("Current balance:",account.get_balance())