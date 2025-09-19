#list in prime number print(1,50)
def primenumber(num):
 isprimenum=True
 if(num<=1):
    print("please give me number")
 else:
    for x in range(2,num):
        if(num%x==0):
          isprimenum=False
        break
    if( isprimenum):
          return True
    else:
          return False
        
op=[x for x in range(2,51) if(primenumber(x))]
print(op)
#tuple in prime number print(1,50)
def primenumber(num):
    isprimenum=True
    if(num<=1):
        print("please give me number")
    else:
        for x in range(2,num):
            if(num%x==0):
                isprimenumber=False
                break
        if(isprimenum):
             return True
        else:
             return False
op=tuple(x for x in range(2,51)if(primenumber(x)))
print(op)#set in prime number print(1,50)
def isprime(num):
    isprimenum=True
    if(num<=1):
        print("ples give me number")
    else:
        for x in range(2,num):
            if(num%x==0):
                isprimenumber=False
                break
            if(isprimenum):
                 return True
            else:
                 return False
op1={x for x in range(2,51)if(primenumber(x))}
print(op1)
#perfect square
num=16
isperfect_squre=False
for i in range(1,num):
    if(i**2==num):
     isperfect_squre=True
     break
if(isperfect_squre):
     print(" it is a perfect number")
else:
     print(" it is not perfect number")
 #sunny number
num=15
issunny=False
for x in range(1,num):
    if(x**2==+1):
        issunny=True
        break
if(issunny):
     print("it is a sunny number")
else:
     print("it is not sunny number")



#neon number
num=9
square=num**2
sum=0
while(square>0):
   ld=square%10
   sum+=ld
   square=square//10
if(sum==num):
    print("it is a neon")
else:
    print("it is not a neon")

            
        
