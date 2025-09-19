#single inheritance.
class parent:
    def pmethod(self):
        print("i am a method from parent")
class child(parent):
    def cmethod(self):
         print("i am a method from child")
obj1=child()
obj1.cmethod()
obj1.pmethod()

#example:

class user:
    def __init__(self,name,email):
            self.name=name
            self.email=email
        
class student(user):
     def __init__(self,name,email,enrolledcoures):
      super().__init__(name,email)
      self.enrolledcourses=enrolledcoures
     def getcourses(self):
       print(f"{self.name} is learning{self.enrolledcourses}")
class instructor(user):
     def __init__(self,name,email,courses_traing):
           super().__init__(name,email)
           self.courses_traing=courses_traing
     def getcourses(self):
            print(f"{self.name} is teaching{self.courses_traing}")
student_obj=student("aneela","anee@gamil.com",["html","css","js","python"])
student_obj.getcourses()
trainer_obj=instructor("harish","harish@gamil.com",{"frontend","backend","database","ai"})
trainer_obj.getcourses()

#remove.
class user:
    def __init__(self,name,email):
            self.name=name
            self.email=email
        
class student(user):
     def __init__(self,name,email,enrolledcoures):
      super().__init__(name,email)
      self.enrolledcourses=enrolledcoures
     def getcourses(self):
       print(f"{self.name} is learning{self.enrolledcourses}")
     def removecourse(self,course):
          self.enrolledcourses.remove(course)
          self.getcourses()
          
class instructor(user):
     def __init__(self,name,email,courses_traing):
           super().__init__(name,email)
           self.courses_traing=courses_traing
     def getcourses(self):
            print(f"{self.name} is teaching{self.courses_traing}")
student_obj=student("aneela","anee@gamil.com",["html","css","js","python"])
student_obj.getcourses()
trainer_obj=instructor("harish","harish@gamil.com",{"frontend","backend","database","ai"})
trainer_obj.getcourses()
student_obj.removecourse("html")



