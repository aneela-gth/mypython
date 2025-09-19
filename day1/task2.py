#1. what will be output of the folling code? and explain why?
x=10
def show():
    x=5
    print(x)
show()
print(x)
#2. what will be the output of the following coge? and explain why?
def outer():
    X=10
    def tnner():
        print(x)
    tnner()

outer()    
#3.what will be the output of the fowwing coding? and explain why?
x="global"
def outer():
    x="outer"
    def tnner():
        x="tinner"
    tnner()
    print("outer:",x)
outer()
print("global:",x)