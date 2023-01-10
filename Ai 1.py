e=input("need to start operation :")
while e=="yes":
    a =int(input("enter a number:"))
    b =int(input("Enter a number:"))
    c =input("Enter your choice + or - or * or / : ")
    if(c=="+"):
        print(a+b)
    elif(c=="-"):
        print(a-b)
    elif(c=="*"):
        print(a*b)
    elif(c=="/"):
        print(a/b)
    else:
        print("invalid")
    e=input("need to do other operations : ")
