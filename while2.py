#prime number or not
num=int(input("enter a number"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("2,num")
            if num%i==0:
             print('not prime')
            break 
    else:
            print("it is prime")
else:
 print("invalide number")
#armstronges numbers
num=int(input("enter a number"))
sum=0
temp=num

