class person:
    name="aneela"
    age="25"
    gender="femial"

obj1=person()
obj2=person()
print(obj1)
print(obj2)
print(obj1.name)
print(obj2.name)

obj1.name="aneela bandi"
#updating value in obj1
print(obj2.name)#does not reflected to object2
print(obj1.name)#reflecting only in obj1
print(person().name)#does not reflect to person class also.



class Application:
    def __init__(app,name,color,catagery):
          app.name=name
          app.color=color
          app.category=catagery
    def purpose(self):
        print("sociesl media purpose")
instagram=Application("instagram","pink","social media")    
youtube=Application("youtube","red","enterainment")
ola=Application("ola","black","travelling")
zomato=Application("zomato","red","food")
print(instagram.name,instagram.color,instagram.category)
print(youtube.name,youtube.color,youtube.category)
print(ola.name,ola.color,ola.category)
print(zomato.name,zomato.color,zomato.category)
print(instagram.name,instagram.color,instagram.category)
instagram.purpose()
ola.purpose()
youtube.purpose()
class Application:
     def __init__(app,name,color,category):
          app.name=name
          app.color=color
          app.color=category
     def purpose(self,app_name,purpose):
      print(f"{app_name} is used for {purpose}")

instagram=Application("instagram","pink","social media")
youtube=Application("youtube","red","entertainment")
ola=Application("ola","black","travel")
zomato=Application("zomoto","red","food")

instagram.purpose("instagram","socialmedia")
youtube.purpose("youtube","entertainment")
ola.purpose("ola","travel")
zomato.purpose("zomato","food")


class phone:
    def __init__(device,name,color,gb,cost):
        device.name=name
        device.color=color
        device.gb=gb
        device.cost=cost
    
    def purpose(self):
        print("mobile purpose")
realme=phone("realme","blue","8gb","39998")
onepluse=phone("onepluse","black","8gb","24998")
apple=phone("apple","wight","128gb","72400")
oppo=phone("oppo","forest green","8gb","3799")
print(realme.name,realme.color,realme.gb,realme.cost)
print(onepluse.name,onepluse.color,onepluse.gb,onepluse.cost)
print(apple.name,apple.color,apple.gb,apple.cost)
print(oppo.name,oppo.color,oppo.gb,oppo.cost)
realme.purpose()


class books:
    def __init__(type,name,autor,eyers):
        type.name=name
        type.autor=autor
        type.reliseddate=eyers


class BankAccount:
    def __init__(acont,name,email,ph,balance):
        acont.name=name
        acont.email=email
        acont.ph=ph
        acont.balance=balance
    def deposit(acont,d_amount):
        acont.balance+=d_amount
    def deposit(acont,w_amount):
        acont.balance-=w_amount
    def checkbalance(acont):
        print(acont.balance)
aneela_acont=BankAccount("aneela","ane@gmail.com",2356647467488)
aneela_acont.checkbalance()
aneela_acont.deposite(500)
aneela_acont.checkbalance()
aneela_acont.withdraw(2000)
aneela_acont.checkbalance()
class parent:
    def pmethod(self):
        print("i am a method from parent")
    def pmethod2(self):
            print("i am a second  method from parent")
class child(parent):
    def cmethod(self):
        print(" i am a method from child")
        super().pmethod2()#calling mehod from super class using supper
obj1=child()
obj1.cmethod()


#create a class dog, and create 3 objectes must have data on their name and their breed.add displayed a dog's bark.

class dog():
    def __init__(self,name,breed):
        self.name=name
        self.bred=breed
    def bark(self):
        print(f"{self.name} is braking")
dog1=dog("max","")