#1.write a simple progarm with two classes(car,biken) and create objects of each.
class car:
    def __init__(self,name,color,brand):
        self.name=name
        self.color=color
        self.brand=brand
    def purpose(self):
        print(f"Car Brand: {self.brand}, Color: {self.color}")

class bike:
    def __init__(self,name,color,brand):
        self.name=name
        self.color=color
        self.brand=brand
    def purpose(self):
         print(f"Car Brand: {self.brand}, Color: {self.color}")


car=car("car","blue","binje")
bike=bike("bike","black","pelusear")
car.purpose()
bike.purpose()

class person:
  name="aneela"
  age=23
  gender="femail"
obj=person
obj.name="bandi aneela"
print(obj.name)

