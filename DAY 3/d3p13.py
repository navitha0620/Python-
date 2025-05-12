#filter()-->

def func(i):
    return i%2==0 
r1=range(1,11)#sequence object
f=filter(func,r1)
#WHATEVER WAS PASSED TO THE FUNCTION WHEN PASSED VALUE IS "TRUE ONLY"


print("First Time")
for ele in f:
    print(ele,end=' ')


print("Second Time")
for ele in f:
    print(ele,end=' ')