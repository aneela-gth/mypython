#1. write a program to check input string is palindrome or not using while loop
str1=input ("enter a string :")
left=0
right=len(str1)-1
is_palindrome=True

while left<right:
    if str1[left]!=str1[right]:
        is_palindrome=False
        break
    left+=1
    right-=1
if is_palindrome:
        print("it is a palindrome")
else:
        print("it is not a palindrome")

#2. write a program to reverse a number without converting into string
num=123
convt=str(num)
for x in  convt:
      print(x)
      for x in range(len(convt)-1,-1,-1):
            print(convt[x])
            print(num%10)
            print(num//10)
while(num>0):
      ld=num%10
      print(ld)
      num=num//10
      