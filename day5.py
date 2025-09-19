list=["hello","welome","something","hello","apple","apple"]
dict={}
for x in list:
    if(x in dict):
        dict[x]+=1
    else:
        dict[x]=1
print(dict)

list="banana"
dict={}
for x in list:
    if(x in dict):
        dict[x]+=1
    else:
        dict[x]=1
print(dict)

