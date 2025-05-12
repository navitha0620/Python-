l2=[10,10,10,10 ,101, 20.4, 30, 40, None, (2+4j), 'Navitha', 15]
print(l2)
#COPY
l1=l2.copy()
print(l1)
#COUNT
l1.count(10)
print("l1 count",l1.count(10))
#EXTEND METHOD
l2.extend([20,15,11,6])
print(l2)
#LENGTH
print(len(l2))
#INDEX
print(l2.index(20.4))
#INSERT
l2.insert(7,5)
print(l2)
#REPLACE
l2[8]=11
print(l2)
#POP REMOVES THE LAST ELEMENT FROM THE LIST
l2.pop()
print(l2)
#POP WITH INDEX
l2.pop(4)
print(l2)
#REMOVE THE ELEMENT WHICH IS SPECIFIED THAT TO FIRST OCCURED ELEMENT
l2.remove(10)
print(l2)
#REVERSE
l2.reverse()
print(l2)
#SORT
l1=[10,5,20,100]
l1.sort()
print(l1)
#CLEAR
l2.clear()
print(l2)

