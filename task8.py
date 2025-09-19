#practice problems(lists&tuples)
#1.add all elementes of a list.
x=[1,3,5,78,45,34]
print(sum(x))
#2.find max and min in a list.
tuple=(21,42,10,8,34,23,12,45,60)
print(max(tuple),min(tuple))
#3. count even ans odd numbers in a list.
x=[2,4,8,9,4,5,1]
count1=0
count2=0
for i in x:
    if(i%2==0):
      count1+=1
    else:
      count2+=1  
print(count1)
print(count2)
#4.reverse a list without using reverse().
list=[1,2,3,4,5]
temp=[]
for i in range(len(list)-1,-1,-1):
  temp.append(list[i])
print("reverse a list:",temp)
#5.remove duplicates from list.
numbers=[1,3,4,1,6,3,1,5,3,2]
print(list(set(numbers)))

#6.sort a list of strings by length.

#7.find the second largest number in the list.
#8.find sum of all nested list elementes.
#9.check if two lists are equal.
#10.merge two lists and sort them.
#11.convert tuple to list and back.
#12.check if the tuple contains a value.