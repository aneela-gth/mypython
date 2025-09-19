#print palandrom
str="madam"
op=""
for chr in range(len(str)-1,-1,-1):
    op+=str[chr]
print(op)
if(op==str):
        print("it is palndrom")
        
else:
        print("it is not palndrom")


#print ovelws print
str="aneela"
for i in str:
       if i in('a','e','i','o','u'):
        print(i)
#print amstrong number   
num=121
n1=num
sum=0
while(num>0):
      ld=num%10
      num=ld**3
      sum+=n1
      num=num//10
if(sum==n1):
      print("it is a amstrong")
else:
      print("it is not amstrong")
#check for prime number
num=int(input("enter a number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print( "prime")
            break
    else:
        print("not prime")
#factorial of a number (using loop)
num=5
fact=1
for i in range(1,num+1):
    fact*=i
    print("factorial",fact)
#check if number is even or odd
x=12
if(x%2==0):
    print("is a eveen")
else:
     print("is odd")


     


      