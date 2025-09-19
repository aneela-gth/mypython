#method overriding

class order:
    def __init__(self,customer,order_id):
        self.customer=customer
        self.order_id=order_id
    def deliver(self):
        print(f"{self.customer} will get his order num {self.order_id} with standard delivery")
class expressorder(order):
    def __init__(self,customer,order_id):
        super().__init__(customer,order_id)
    def deliver(self):
         print(f"{self.customer} will get his order num {self.order_id} with express delivery in one day/same day")
obj1=order("aneela","a12e")
obj2=order("harish","nar123")
obj=expressorder("nares","nari85")
print(obj1.__dict__)
print(obj2.__dict__)
print(expressorder.__mro__)

#encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner         
        self.__balance = balance  
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
acc = BankAccount("Aneela", 5000)
print("Account holder:", acc.owner)
print("Current Balance:", acc.get_balance())
acc.deposit(2000)
acc.withdraw(1000)
acc.withdraw(10000)
#public
class sample:
    def __init__(self):
        self.name="aneela"
obj=sample()
print(obj.name)
#protting
class sample:
    def __init__(self):
        self._name="sreevani"
obj=sample()
print(obj._name)
#pravet
class sample:
    def __init__(self):
        self.__name="suppu"
obj=sample()
print(obj._sample__name)

#geter 
class demo:
    def __init__(self):
     self.__name="harish"
     obj=demo()
    print(obj.__dict__)
    obj.__name="kirean"
print(obj.__dict__)
#seter
class demo:
    def __init__(self):
     self.__name="harish"
    def setdetails(self):
        self.__name="kirean"
obj=demo()
print(obj.__dict__)
obj.setdetails()
print(obj.__dict__)
