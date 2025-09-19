
'''def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("enter a number"))
print(isprime(n))'''


'''def isprime(x):
    if x<=1:
        return False
    for i in range(1,x+1):
        if x%i==0:
            return False
    return True
count=0
for i in range(x1,x2+1):
 count+=1
 print("")
x=int(input("enter a number"))
print()'''

'''n1="111"
n2="100"
sum=0
j=0
for i in range(len(n1)-1,-1,-1):
    sum+=int(n1[i]*(2**j))
    j+=1
    k=0
    for i in range(len(n2)-1,-1,-1):
        sum+=int(n2[i]*(2**k))
        k+=1
    print(str(bin(sum)[2:]))'''

x="sraaavan"
res=x[0]
c=1
for i in range(1,len(x)):
    if x[i]==x[i-1]:
        c+=1
        if c<3:
            res+=x[i]
    else:
            c=1
            res+=x[i]
print(res)

x="aneeela"
res=x[0]
c=1
for i in range(1,len(x)):
    if x[i]==x[i-1]:
        c+=1
        if c<3:
            res+=x[i]
    else:
            c=1
            res+=x[i]
print(res)

a=2
t-c=4
w=a
while w>=3:
    e=w//3
    t-c+=3
    w=e+e%3
print(t-c)
2