for x in range(1,6):
    str=0
    for y in range(x):
        str=str*10+x
    print(str)


for x in range(1,6):
        str=0  
        for y in range(1,x):
            str=str*10+y
print(str)

'''for x in range(97,102):
         str=""
         for y in range(x,x+1):
          str+=chr(x)
         print(str)'''

'''for i in range(1**2,9*2):
    str=0
    for y in range(i):
         str=str*10+y
           
    print(str)'''

'''num=int(input("enter a number:"))
for i in range(num+1,0,-1):
   for j in range(1,i+1):
      print(j*j,end=" ")
   print()

num=int(input("enter a number:"))
for i in range(1,num+1):
   for j in range(1,i+1):
      print(j*j,end=" ")
   print()

num=int(input("enter a number:"))
for i in range(1,num+1):
   for j in range(1,i+1):
      print(j,end=" ")
   print()

num=int(input("enter a number"))
for i in range(1,i+1):
    for j in range(1,i+1):
        print(i+j,end="")
    print()

num=int(input("enter a number"))
for i in range(1,i+1):
    for j in range(1,i+1):
        print(j-1,end="")
    print()'''

num=int(input("enter a number"))
for i in range(1,num):
    for j in range(1,i+2):
        print(i*i)
    print()