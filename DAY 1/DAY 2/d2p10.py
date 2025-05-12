#UNPACKING
def func(a,b=0,c=0):#b=0,c=0 MEANS DEFAULT PARAMETERS
    return a+b+c
    pass
#---->func([10,20,30])#PASSING LIST AS AN ARGUMENT TO A FUNCTION--->REQUIRED PARAMETERS
add=func(10)
print(add)
print( func(10,20) )
add1=func([10,20,30],[10,20,40],[20,4,5])#LIST AND LIST CAN BE CONCATENATE
print(add1)
x=func(*[10,20,30])#func(10,20,30)-->UNPACKING
print(x)
