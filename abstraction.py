#abstraction
'''from abc import ABC, abstractmethod
class waterfilter(ABC):
    @abstractmethod
    def waterpasser(self):
        pass
class coldwater(waterfilter):
    def waterpasser(self):
        print("cold water served")
class hotwater(waterfilter):
    def waterpasser(self):
        print("hot water served")
class normalwater(waterfilter):
    def waterpasser(self):
        print("normal water served")
c=coldwater()
h=hotwater()
n=normalwater()
c.waterpasser()
h.waterpasser()
n.waterpasser()

from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def towheeler(self):
        pass
class bike(vehicle):
    def towheeler(self):
        print("ried in  bike")
class car(vehicle):
    def towheeler(self):
        print("riding in car")
class bus(vehicle):
    def towheeler(self):
        print("group of members are traveled")

Bike=bike()
Car=car()
Bus=bus()
Bike.towheeler()
Car.towheeler()    
Bus.towheeler()


from abc import ABC,abstractmethod
class employe(ABC):
    @abstractmethod
    def get_salary(self):
        pass
    def work(self):
        pass
class manager(employe):
    def get_salary(self):
        return 70000
    def work(self):
        print("manager is planning and orginizing tem tasks.")
class developer(employe):
    def get_salary(self):
        return 60000
    def wor(self):
        print("devlopers  is writting and testing code. ")
m=manager()
d=developer()
print("manager salary:",m.get_salary())
m.work()
print("developer salary:",d.get_salary())
d.work()

#2 polymorphism

class dog():
    def speak(self):
        return "woof!!"
class cat():
    def  speak(self):
       return "meow!!"
class tigger():
    def speak(self):
        return "roars"
    def animal_sounds(animals):
      print(animals.speak())
    dog=dog()
    cat=cat()
    #tigger=tigger()
    animal_sounds(dog)
    animal_sounds(cat)
    #animal_sounds(tigger)'''



'''import random
class bank:
    T_holders=[] #class variable
    def create_new_account(self):
        H_details={}
        data=random.randint(100000000000,999999999999)
        H_details["h_name"]=input("enter holder name:")
        H_details["mobile_no"]=input("enter mobile number:")
        H_details["aadhar_no"]=input("enter aadhar number:")
        H_details["account_number"]=data
        H_details["IFSC"]="IFSC05236"

        acc_type=input("select type of account(saving/zero):").lower()
        while True:
            if acc_type=="saving":
                amount=int(input("deposit 1000 rupes...."))
                if amount==1000:
                  H_details["balance"]=amount
                  break
                else:
                 print("deposit 1000 rupes.......")
            elif acc_type=="zero":
                amount=int(input("deposite 500 rupes........"))
                if amount==500:
                  H_details["balance"]=amount
                  break 
                else:
                 print("deposit exatly 500 rupes for zero balance account.")
            else:
               print("invalid account type. plece entern 'saving' or 'zero'")
        bank.T_holders.append(H_details)
        print("account created successfully!")
        print(bank.T_holders)
obj=bank()
obj.create_new_account()'''

'''# Single Inheritance
class Parent:
    def display_parent(self):
        print("This is the Parent class.")

class Child(Parent):
    def display_child(self):
        print("This is the Child class.")

obj = Child()
obj.display_parent()  
obj.display_child()   


# Multiple Inheritance
class Father:
    def father_details(self):
        print("Father: Works in IT.")

class Mother:
    def mother_details(self):
        print("Mother: Works in Education.")

class Child(Father, Mother):
    def child_details(self):
        print("Child: Loves Coding.")

obj = Child()
obj.father_details()
obj.mother_details()
obj.child_details()


# Multilevel Inheritance
class GrandParent:
    def show_grandparent(self):
        print("GrandParent: Retired Army Officer.")

class Parent(GrandParent):
    def show_parent(self):
        print("Parent: Business Owner.")

class Child(Parent):
    def show_child(self):
        print("Child: Student.")

obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()

# Hierarchical Inheritance
class Parent:
    def parent_info(self):
        print("Parent: Loves Gardening.")

class Child1(Parent):
    def child1_info(self):
        print("Child1: Plays Cricket.")

class Child2(Parent):
    def child2_info(self):
        print("Child2: Plays Chess.")

obj1 = Child1()
obj1.parent_info()
obj1.child1_info()

obj2 = Child2()
obj2.parent_info()
obj2.child2_info()
# Hybrid Inheritance
class GrandParent:
    def gp_info(self):
        print("GrandParent: Retired Teacher.")

class Parent1(GrandParent):
    def p1_info(self):
        print("Parent1: Engineer.")

class Parent2:
    def p2_info(self):
        print("Parent2: Doctor.")

class Child(Parent1, Parent2):
    def child_info(self):
        print("Child: Artist.")

obj = Child()
obj.gp_info()
obj.p1_info()
obj.p2_info()
obj.child_info()'''

#overriding
class Animal:
    def make_sound(self):
        print("Some generic animal sound")
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")
a = Animal()
a.make_sound()  
d = Dog()
d.make_sound()   
c = Cat()
c.make_sound()   
#2. Encapsulation

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder   
        self._account_type = "Savings"         
        self.__balance = balance               
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.__balance}")
        else:
            print("Invalid withdrawal amount.")
    def get_balance(self):  
        return self.__balance
acc = BankAccount("Aneela", 5000)
acc.deposit(1500)      
acc.withdraw(2000)      
print(acc.get_balance())
print(acc.account_holder)  
print(acc._account_type)    

























    