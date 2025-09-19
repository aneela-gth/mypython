#1. wap to check whether givean number is armstrong or not
num=int(input("entear a number"))
sum=0
temp=num
n=len(str(num))
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp=temp//10
if sum==sum:
   print(" armstrong")
else:
   print(" not armstrong")
#2.check what is nean numbear and sunny number
#nean number
num=9
square=num**2
sum=0
temp=square
while square>0:
    ld=square%10
    sum+=ld
    square=square//10
if sum==num:
  print(" it is a neon number")
else:
  print(" it is not nean number")

#sunny number
num=15
is_sunny=False
for x in range(1,num):
        if(x**2==num+1):
           is_sunny=True
           break
if(is_sunny):
    print("it is a sunny number")
else:
     print("it is not a sunny number")
