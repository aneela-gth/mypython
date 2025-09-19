for x in range(1,11):
   print(f"2x{x}={2*x}")
   def mul():
       for x in range(1,11):
            print(f"{"num"}x{x}={"num*x"}")
            mul("num")
for x in range(1,11):
    print(x**2)
    for x in (1,21):
        if(x%2==0 and x%3==0):
            print(f"{x} -fizz")
        elif(x%3==0):
            print(f"{x}-buzz")
        elif(x%2==0):
            print( f"{x}-fizz")
total=0
for x in range(1,11):
        total+=x
print(f"toteal natural number:",total)
total=0
for i in range(1,11):
    x=i**2
    total+=x
print(f"square of the value:",total)

for i in range(1,101):
    squae_root=i**0.5
    if(i**0.5):
        print(i)
        

#evers string
i=["a","b","c","d","e"]
for i in range(len(i)-1,-1,-1):
    print(i['x'])
    
    str="hello"
    op=""
    for char in range(len(str)-1,-1,-1):
        op+=(str[char])
        print(op)
str="madam"
op=""
for char in range (len(str)-1,-1,-1):
     op+=str[char]
     print(op)
     if(op==str):
          print("it is palindrome")
     else:
          print("it is not a palindrome")

          