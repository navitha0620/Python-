#map()--->Map is a class name 
def func(i):
    return i**3
r1=range(1,11)#sequence object
m=map(func,r1)#r1 is passing to func function
#IT WILL COLECT ALL  RETURNED ELEMENT OR OBJECTS AND STORED IN "map OBJECT"
print(m)

#Map object is iterable object 
print("First Time")
for ele in m:
    print(ele)

#MAP OBJECTS ARE ONE TIME USEABLE OBJECTS >>>WE CANT GET SECOND TIME 
#If we try to print second time means it means it is empty or deleted 
print("second time")
for ele in m:
    print(ele)