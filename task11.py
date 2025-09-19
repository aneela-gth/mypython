#add two number
a=5
b=2
print("sum",a+b)
#check if number is even or odd
x=12
if(x%2==0):
    print("is a eveen")
else:
    print("it is odd ")
#find the largest of 3 numbers
'''x=2
y=3
z=1
laregest=max(x,y,z)
print("largest:"largest)'''
#print number 1 to 10 using for loop
for i in range(1,11):
    print(i)
#sum of all number in a list
num=[12,43,22,21]
total=sum(num)
print("total",total)
#factorial of a number (using loop)
num=5
fact=1
for i in range(1,num+1):
    fact*=i
    print("factorial",fact)
#check for prime number
num=int(input("enter a number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
        else:
            print("prime")
    else:
        print("not prime")
