import random
#1.generate 5 random floats between 0 to t
for i in range(5):
    i=random.uniform(0,1)
    print(i)


#2.dice roll simulator using random.randint
dice=random.randint(1,6)
print('dice roll simulator:',dice)


import math
#3.convert 90 degrees to radians
print(math.radians(90))


#4.factorial of a user-given number
num=int(input("enter a number:"))
print(math.factorial(num))


#5.shuffle a list of 10 integers
list=[10,20,30,40,50,60,70,80,90,100]
random.shuffle(list)
print(list)


#1.lottery draw of 6 unique numbers from 1 to 49
num=random.sample(range(1,50),6)
print('lottery draw numbers are:',num)


#2.approximate using monte carlo
inside=0
total=10000
for i in range(total):
    x=random.random()
    y=random.random()
    if x*x+y*y<=1:
        inside+=1
pi_approx=(inside/total)*4
print("approximated pi:",pi_approx)




# 3. Calculate compound interest using math.pow
p=100
r=0.05
t=3
n=1
CI=p*math.pow((1+r/n),n*t)
print("compound interest:",CI)


# 4. Trigonometry calculator using degrees
angle=45
radians=math.radians(angle)
print("sin:",math.sin(radians))
print("cos:",math.cos(radians))
print("tan:",math.tan(radians))


#  5. Roll two dice 1000 times and plot the sum frequency


counts=[0]*13
for i in range(1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    total=dice1+dice2
    counts[total]+=1
print("sum\tcount")
for i in range(2,13):
    print(f"{i}\t{counts[i]}")











