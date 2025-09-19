fruits =["apple","mango","banana"]
print( fruits[0])
print(fruits[2])
print(len(fruits)) 
fruits[1]="pineapple"  
print(fruits)

x=["harish","naresh","suresh","mahesh"]
x[2]="kiran"
print(x)

data=[1,2,[4,5],[6,7],8,["something"]]
print(data[2][0])
print(data[3][1])
print(data[5][0][2])

mixed=[1,2,"hi",12.5,True]
print(f"value:{mixed[0]},type:{type(mixed[0])}")
print(f"value:{mixed[2]},type:{type(mixed[2])}")