#cretea class and object
class Bank:
    def __init__(self, name):
        self.name = name
    def show_bank(self):
        print(f"{self.name} is a national bank.")
class Account(Bank):
    def __init__(self, name, acc_no, balance):
        super().__init__(name)
        self.acc_no = acc_no
        self.balance = balance
    def show_account(self):
        print(f"Account No: {self.acc_no}, Balance: ₹{self.balance}")
a = Account("SBI", "123456789", 5000)
a.show_bank()
a.show_account()
# multiple inheritance
class camera:
    def take_photo(self):
        print("photo capuctured")
class musicplayer:
    def play_music(self):
        print("playing music")
class smartphone(camera,musicplayer):
    def make_call(self):
        print("calling...")
s=smartphone()
s.take_photo()
s.play_music()
s.make_call()
#multileveal inheritance
class Platform:
    def platform_info(self):
        print("Platform: LearnOnline")
class Course(Platform):
    def course_info(self):
        print("Course: Python Programming")
class Student(Course):
    def student_info(self):
        print("Student: Aneela")
s = Student()
s.platform_info()
s.course_info()
s.student_info()
#4. Hierarchical Inheritance
class Employee:
    def base_salary(self):
        print("Base Salary: ₹20,000")
class Manager(Employee):
    def manager_bonus(self):
        print("Manager Bonus: ₹10,000")
class Developer(Employee):
    def dev_bonus(self):
        print("Developer Bonus: ₹8,000")
m = Manager()
d = Developer()
m.base_salary()
#5. Hybrid Inheritance
class Person:
    def details(self):
        print("Person: General info")
class Staff(Person):
    def staff_info(self):
        print("Works in admin department")
class Student(Person):
    def student_info(self):
        print("Studies in 10th class")
class SchoolMember(Staff, Student):
    def member_role(self):
        print("School Member with dual role")
