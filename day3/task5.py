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

