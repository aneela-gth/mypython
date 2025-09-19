for x in range(1,10):
    print(x)
    if(x==5):
        break

    for i in range(1,10):
        if(i==5):
            break
        print(x)


for x in range(1,10):
    print(x)
    if(x==5):
        continue 
    print(x)

    for x in range(1,10):
        if(x==5):
            continue
        x+=1
        print(x)

        stop=["kphb","srnagar","ameerpet","parade ground","paradise","sec"]
        for stop in stop:
            if(stop=="ameerpet"):
                print("stop")
                
        stop=["kphb","srnagar","ameerpet","parade ground","paradise","sec"]
        for stop in stop:
            if(stop=="ameerpet"):
                continue
        print(stop)

for x in range(1,10):
    print(x)
    if(x==5):
        break
    str="madam"
    op="" 
    for char in range(len(str)-1,-1,-1):
        op+=str[char]
        print(op)
        if(op==str):
            print("it is palindrome")
        else:
            print("it is not a palindrome")
