#list functions
#append()
list1=[1,2,3,4,5]
list1.append(6)
print(list1)
#extend()
list1.extend([7,8,9,10])
print(list1)
#insert()
list1.insert(1,300)
print(list1)
#remove()
list1.remove(300)
print(list1)
#pop()
list1=[1,2,1,4,4,6,1,5]
list1.pop(5)
print(list1)

list1=[1,13,1,5,7,6]
a=list1.pop()
print(a)
#count()
list=[1,2,1,3,1,4,1,5]
print(list.count(1))
#clear()
list1.clear()
print(list1)
#tuple functions
tuple1=(1,2,3,4,5)
print(tuple1.index(3))
#packing()
data=1,5,6,7,3,9
print(data)
#unpacking()
data=1,2,3,4,5
print(a)
a,b,c,d,e=data
print(a)
print(b)

a,*b,c=data
print(a)
print(b)
print(c)