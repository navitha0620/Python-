a=int(input("a:\t"))
b=int(input("b:\t"))
c=int(input("c:\t"))
if(a>b and a>c):
    print("a is greater than b and c")
elif(b>c):
    print("b is greater than c and a")
elif(c>b):
    print("c is greater than a and b") 
elif(a<b):
    print("c is greater than a and b")
else:
    print("a is greater than c and b")