op=lambda:print("hellow")
print(op())

op=lambda:"hi"
print(op())

op=lambda x:x+2
print(op(4))
op=lambda x,y:x+y
print(op(4,5))
op=lambda x:"even"if x%2==0 else"odd"
print(op(5))

def func1():
    print('x')

    func1()

    def sample():
        x=5
        print("hellow")
        sample()
        print(x)

        def func1():
            print(x)
            def func2():
                x=10
                func1()
                func2()
                
                def func1():
                    global x
                    x=10
                    func1()
                    print(x)
                    def fun():
                        x=5
                        def func1():
                            x=10
                            func2()
                            print(x)
                            func1()