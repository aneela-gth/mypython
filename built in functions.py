#1. with using function count the number of values in string
a="aneela"
count=0
for i in a:
    count=count+1
    print(count)
#2. with using function count the number of values in string
    a="aneela"
    print(len(a))
#3. int convert  value into an integer
a=10.0
b=3+4j
c="10"
print(int(a))
print(int(c))
#4.float value conver into a integer
valu1=20
valu2=30
print(float (valu1))
print(float(valu2))
#5.int value conver into complex
x=20
y=40
print(complex(x,y))
print(complex(x))
z=complex(x,y)
print(complex(x,y))
print(z)
#6. float value convert into a absolute
a=-10.23
print(abs(a))

a=-10.23
b=10
print(abs(a),abs(b))
c=3+4j
print(abs(c))
#7. it reises a value to the power of value possed next to it.
s=20
p=5
print(pow(s,p))
#8.it returns the quotient and remainde of a division operaction.
x=40
y=4
print(divmod(40,4))
#9.round up too the nearest integer value,or to a specific number of decimal values.
valu1=20.5
value2=9.8
print(round(valu1),(round(valu2)))
valu3=3.15678903
print(round(valu3))

a=6.5
b=3.4
c=9.8
print(round(a),round(b),round(c))
#10.min() and max() returns the minimum and maximum values in a sequence of elementes.
tuple1=(10,35,98,27,56,23)
print(max(tuple1),min(tuple1))