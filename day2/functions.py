#add two numbers
def add(a,b):
    return(a+b)
print(add(5,3))

#check even or odd
def is_even(n):
    return n%2==0
print("is_eveen")

#largest  of three numbers
def largest(a,b,c):
    return max(a,b,c)
print(largest(5,12,8))

#area of a circle
import math
def area_of_circlr(radius):
    return math.pi*radius*radius
print("area_of_circle(3)")

#celsius to fahrenheit
def celsius_to_fahrenheit(celsisus):
    return(celsisus*9/5)+32
print(celsius_to_fahrenheit(0))
#square of a number 
def square(n):
    return n**2
print("sruare(4)")
#cub of a number
def cub(n):
    return n**3
print("cub(3)")

#reverse a string
def reveres_string(s):
    return s[::-1]
print("hello")

#palindrom check
def is_palindrom(s):
    return s==s[::-1]
print("madam")

def lep_eyer(year):
    if(year%4==0 and year%100!=0):
        print("lep_year")
    else:
        print("not lep year")
        
        def modify(x):
            x=x+10
            print("changed value:,x")
            a=7
            modify(a)
            print("origins=al value:,a")

#arbitary argumrentes/*args
def add(*numbers):
    print(sum(numbers))
add(1,2,3,4,6,7,56,87)

def stationary(*price):
    print(len(price))
    print(sum(price))
stationary(3,5,10,20)

def details(*details, batch=53):
    print(batch)
    print(details)
details("rama",12,"python")

 #**keyword arguments
def details(**details):
        print(details)
details(name="rama",batch="52",cource="python")

def detiles(**details):
            print(details)
details(name="rama",age="21",cource="python")
