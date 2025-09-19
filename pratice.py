def name():
    a=2
    b=4
    print(a+b)
name()
def is_even(a):
    if(a%2==0):
        print("even")
    else:
        print("odd")
is_even(10)
def is_odd(b):
    if(b%2==0):
        print("even")
    else:
        print("odd")
is_odd(3)
for i in range(1,6):
    print(i)


for i in range(1,10):
        print(i)
for i in range(1,5):
    print(i**2)
for i in range(1,10):
    if(i%2==0):
        print(i**2,"squares")
    else:
        print(i**3,"cubes")      


#1.
    x=15
    if x%3==0 and x%5==0:
        print("fizzbuss")
#2. 
    lst=[1,2,3]
    print(len(lst))
    lst.append(4)
    print(lst[-1])
#3.
    def compare(a,b):
        if a>b:
            return 'a'
        else:
            return'b'
print(compare(7,5))
#4.

