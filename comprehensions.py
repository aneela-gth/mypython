op=[x+2 for x in range (1,10)]
print(op)

x=[i+1 for i in range(1,20) ]
print(x)
#creat a list of sqares of numbers from 1to20 using comprehensions.
op=[x**2 for x in range (1,21)]
print(op)

list=["hai","aneela","ramu","sharanya","suppu","sreevani"]
op=[x.upper() for x in list]
print(op)
op=[x**2 for x in range(10,31) if x%2==0]
print(op)

list=["hai","aneela","ramu","sharanya","suppu","sreevani"]
op=[x.upper() for x in list if len(x)%2==0]
print(op)

def vowelcount(ip):
  count=0
  for x in ip:
      if(x in ['a','e','i','o','u']):
       count+=1
  if(count%2==0):
    return True
  else:
     return False
list1=["hai","aneela","ramu","sharanya","suppu","sreevani"]
op1=[x.upper() for x in list1 if vowelcount(x)]
print(op1)

#1.creat a list of aemstrong number from 100 to 1000
def armstrong(num):
 temp=num
 n=len(str(num))
 sum=0
 while temp>0:
    digit=temp%10
    sum+=digit**n
    temp=temp//10
 if num==sum:
   return True
 else:
  return False
op=[x for x in range(100,1000)if armstrong(x)]
print(op)
#create list of perfectsrures.
def is_perfect(num):
    is_perfect=False
    for x in range(1,num):
        if(x**2==num):
            is_perfect=True
            break
    if(is_perfect):
        return True
    else:
        return False
op1=[x for x in range(1,50)if(is_perfect(x))]
print(op1)
#create list of neon.
def is_neon(num): 
    square=num**2
    sum=0
    while(square>0):  
        ld =square%10 
        sum+=ld
        square=square//10
        if(sum==num):
           return True
        else:
           return False
op=[x for x in range(1,25)if(is_neon(x))] 
print(op)       
#create list ofsunny number using comprehensions.
def is_sunny(num):
    is_sunny=False
    for x in range(1,num):
        if(x**2==num+1):
            is_sunny=True
            break
    if(is_sunny):
        return True
    else:
        return False
op=[x for x in range(1,24)if(is_sunny(x))]
print(op)
#create list of reversed string using compranctions
list=["anee","anu","suppu","ramya"]
def reversed_string(x):
          rev=""
          for i in range(len(x)-1,-1,-1):
              rev+=x[i]
          return rev     
op=[reversed_string(x) for x in list]
print(op)


 
