# #1.wrie a program to print"hello, world!
# str="hello"
# print(str)
# #2.write a program to add two  numbers entered by the user.
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# print(a+b)
#3.write a program to find the square and cube of number.
# for i in range(1,10):
#   if(i**2==0)and(i**3==0):
#     print("sruares,cubes")
#   else:
#     print("")
# n=int(input("enter a number: "))
# a=n**2 
# b=n**3
# print(a,b)
# #4.write a program to check if  number among three numbers.
# # for nani in range(1,11):
# #     print(nani)

# a=1221
# aneela=a
# rev=0
# while a>0:
#     ls=a%10
#     rev=rev*10+ls
#     a=a//10
# if aneela==rev:
#     print("palindrome")
# else:
#     print("not")

a=121
b=str(a)
rev=" "
for i in ((len(b)-1),-1,-1):
    rev.append(b[i])
    print(rev)
    
    



