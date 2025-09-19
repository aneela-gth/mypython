#1. ceil function
import math
print(math.ceil(4.2))
print(math.ceil(5.23456))
print(math.ceil(0.4579))
#2.floor functions
print(math.floor(9.5))
print(math.floor(34.976))
#3.frunc() functions
print(math.trunc(34.546))
print(math.trunc(5.2))
#4. factorial functions
print(math.factorial(5))
print(math.factorial(8))
print(math.factorial(3))
#5.mathematical constrantes
print(math.pi)
print(math.e)
print(math.nan)
print(math.inf)
#logarithm functions
#6.exp function
print(pow(math.e,10))
print(math.exp(10))

#7.log functions
print(math.log(8,2))
print(math.log(9,3))
#8.sqrt function
print(math.sqrt(25))
print(math.sqrt(54))
#9.trignometic functions
a=math.degrees(90)
b=math.pi
print(round(math.sin(b/2)))
print(round(math.cos(b/2)))
print(round(math.tan(b/2)))
#10.radians function
a=math.radians(90)
print(math.radians(90))
#11.random module functions
import random
print(random.random())
#12.randint function
print(random.randint(10,20))
#13.choice functions
a=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(a))
#14.choies fonctions
a=[1,2,3,4,5,6,7,8,9,10]
print(random.choices(a,k=5))
#16. sample functions
a=[1,2,3,4,5,6,7,8,9,10]
print(random.sample(a,k=5))
#17.shuffle function
a=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(a)
print(a)