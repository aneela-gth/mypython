#1.string functions.
str="aneela"
print(len(str))
str="aneela"
print(str.upper())
x="AKHILA"
print(x.lower())
y="*****ramu join cource*****"
print(y.strip("*"))
y="*****hello world*****"
print(y.rstrip("*"))
a="****you are students****"
print(a.lstrip("*"))
str="i am learnig java"
print(str.replace("java","python"))
list1=["i","am","a","python","student"]
print("".join("list1"))
#2.dictinary functiones.
dict={"name":"aneela","courcr":"python","city":"hyd"}
print(len(dict))
print(dict.keys())
dict={"name":"aneela","courcr":"python","city":"hyd"}
print(dict.values())
dict1={"name":"aneela","courcr":"python","city":"hyd"}
dict2={"phone number":"123456782","addres":"hyd"}
dict1.update(dict2)
print(dict1)
dict1={"name":"aneela","courcr":"python","city":"hyd"}
dict1.clear()
print(dict1)
#3.set functioes.
a={1,2,3,4,5,5}
print(type(a))
set={1,2,3,4,5,}
set.add(6)
print(set)
x={1,2,3,4,5}
x.update([9,8],[5,6],{23,45})
print(x)
x={1,2,3,4,5,}
x.discard(2)
print(x)