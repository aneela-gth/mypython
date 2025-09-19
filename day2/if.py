num=int(input("enter a number"))
if(num>0):
    if(num%2==0):
     print("num is evven  and positive")
    else:
     print("num is odd and positive")
elif(num<0):
 if (num%2==0):
     print("num is evven and negative")
 else:
     print("num is odd and negitive")
else:
  print("u have entered zero") 
 # age group classifier
age=int(input("enter your age"))
x=int(input("enter the age"))
if(x<=0):
    print("invealid")
elif(x<=12):
    print("kides")
elif(x<=19):
    print("teenage")
elif(x<=40):
    print("young")
elif(x<=60):
    print("prime")
else:
    print("rip")
#grade evaluator
m1=int(input("entter the sub1 markes:"))
m2=int(input("enter the sub2 marks:"))
m3=int(input("enter the sub3 markes:"))
m4=int(input("enter youe sub4 markes"))
m5=int(input("enter the  sub5 markes:"))
m6=int(input("enter the sub6 markes"))
totel=m1+m2+m3+m4+m5+m6
p=(totel/600)*100
if(p>=90):
    print("A grade")
elif(p>=80):
    print("B grade")
elif(p>=70):
    print("C grade")
elif(p>=60):
    print("D grade")
else:
    print("Fail")
#triangle type  checkers:
a=int(input("enter value a:"))
b=int(input("enter value b:"))
c=int(input("enter value c"))
if(a==b==c):
  print("we can from equilaterul traiangle")
elif((a==b)or(b==c)or(c==a)):
    print("we can from isosceles trianogle")
elif(a!=b!=c):
    print("sdalene triangle")
elif(((a+b)>=c)or((b+c)>=a)or((c+a>=b))):
    print("inquali triangle")
else:
    print("can not from a triangle")
#ATM withdrawal simulatur:
balance=25000
withdrawal=int(input("ente withdrawal amount"))
if(balance>withdrawal):
    if(withdrawal%100==0):
        print(f"rupes{"withdraw"}successfull withdrawn")
    else:
        print("withdraw amount should be multiple of 100 only")
else:
    print("insufficient blance")
 #problems based on functions:
 #1.writ a function to greet the user.(nno need of parameters)
def greet():
    return"hellow,how are you!"
print(greet())
#2.basic arithemetic operations:
def calculator(a,b,op):
    if(op=='+'):
        return a+b
    elif(op=='-'):
        return a-b
    elif(op=='*'):
        return a*b
    elif(op=='/'):
        return a/b
    else:
        return"invalid operator"
    print("calculator(4,5'*')")
#3.Write a function to wish a student based on his name and the program he chooses to studyUser must be able to give student name and the program name(Mechanical, Civil, Computer Science, ECE, etc.)If no arguments given, the function must wish student with words ‘Student’ and ‘Engineering’ in place of his name and program
def greet (studen_tname='student',branch='engineering'):
    print(f"hello{"student_name"},hope you doing good in {"branch"} program")
    st=input("enter student name:")
    br=input("enter branch name:")
greet("aneela","engineerinng5")
#4.write a function to print user's and age of the  user in 2035(after 10 years from now):
def detiles( name,age): 
 frutur_eyer=2035
 current_eyer=2025
 frutur_age=age+("frutur_age-current_age")
 print (f"{"nme"} wil be {"future_age"} years old in {"future_age"}")
detiles("anee,23")

#5.
def studentdetiles(name,age,phno,ad,bg):
 print( f"name of student{"name"}")
 print(f"age of the student{"age"}")
 print(f"phno of the student{"phno"}")
 print(f"ed of the student{"ed"}")
 print(f"bg of the student{"bg"}")
studentdetiles(name="aneela",age=23,phno=7674087691,ad="anee@4010",bg="A+")
 



