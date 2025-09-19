#1.problems on int()
x=30.4
print(int(x))
#1. convet  a  floating point number (e.g.,4.89)to an integer
x=4.89
print(int(x))
#2.convert a string "7" to int and mulitily it by 5
str="7"
print(int(str)*5)
#problems on float()
#convert an integer input to float
x=8
print(float(x))
#4.convert string '3.1415' to float add 1
str="3.1415"
print(float(str)+1)
#3.problems on complex()
x=10
y=20
print(complex(x,y))
#5.create a complex number form real and imaginary inputs.
value1=4
value2=2
print(complex(value1,value2))
#6.retun square of a complex number using complex
x=2
y=5
print(complex(2,5)**2)
#4.problrms on round()
#7. round 6.72849 to 2 decimial places
x=6.72849
print(round(x))
#8.round user_input float to nearest integer.
a=5
b=3
print(round(a),round(b))
#5.problems on min()and max()
tuple1=(10,35,46,24,14,96,62,55)
print(max(tuple1),min(tuple1))
#9. find min and max from[2,5,1,9,-3,6]
x=[2,5,1,9,-3,6]
print(max(x),min(x))
#10.find the largest of three numbers using max()
x=23
y=10
z=15
print(max(x,y,z))
#11.find alphabetically first name["zara","bob","alice"]
name=["zara","bob","alice"]
print("")
#6.problems on pow()
#12.find 2**5 using pow()
a=20
b=4
print(pow(a,b))
#13.get base and exponent from user, retun result.
base=3
exponent=2
print(base,exponent)
#14.use pow(x,y,z)to find (x**y)%z with inputs x=2,y=3,z=5.
x=2
y=3
z=5
print()
#7. problems on divmod()
#15. use divmod() for 23 divided by 5.
x=23
y=5
print( divmod(23,5))
#16.wrie function to return quotient and remainder.
a=10
b=5
print(divmod(10,5))
#17. convert number to binary using repeated divmod(num,2)

#8.problems on abs()
#18.print absolute value of a user_input number.
a=3+6j
print(abs(a))
#19.get absolute difference between two numbers.
a=10.6
b=10
print(abs(a)-abs(b))
#20.compute manhattan distance from(x,y)to origin.
x=20.4
y=30.5
print(abs(x)+abs(y))
#bonus practice.
#21. multiply two string inputs as integers.
a=3
b=5
print(a*b)
#22. round pow(5,3)/7 to 3 decimal piaces.
result=pow(5,3)/7
round_result=round(result,3)
#23.print largest absolute value from[-2,-8,3,7].
y=[-2,-8,3,7]
largest_abs=max(y,key=abs)
print( abs(largest_abs))

#24.round user float input. then use as exponent for 2.
a=4.6
b=2
print(round(a),round(b))