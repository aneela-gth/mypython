class vehicle:
    def start(self):
        print("vehiceal started")

class car(vehicle):
    def drive(self):
        print("car is driving")
class bike(vehicle):
    def ride(self):
        print("bike is riding")
car=car()
bike=bike()
car.start()
car.drive()
bike.start()
bike.ride()

class account:
    def open_account(self):
        print("account opend")
class savingaccount(account):
    def interest(self):
        print("saving account:interest is 5%")
s=savingaccount()
s.open_account()
s.interest()

#HYBRID INHERITANCE
class Person:
    def person_info(self, name):
        self.name = name
        print(f"Name: {self.name}")

class Teacher(Person):
    def teach(self):
        print("Teaching subjects")

class Student(Person):
    def study(self):
        print("Studying subjects")

class TeachingAssistant(Teacher, Student):
    def assist(self):
        print("Assisting in labs")

# Object
ta = TeachingAssistant()
ta.person_info("Anjali")
ta.teach()
ta.study()
ta.assist()


       