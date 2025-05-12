l1=[1,2,3]
#APPEND
l1.append(4)
print("l1 append:\t",l1)
#USING FOR PRINTING ALL ELEMENTS IN THE LIST
for i in l1:
    print(i)
#PRINT THE ELEMENT IN THE INDEX
l2=l1.index(4)
print("l1 list index element",l2)
#COUNT & INSERT
l1.count(4)
print("l1.count of element 4 is:\t",l1.count(4))
l1.insert(3,8)
print("Inserting the elements in the l1:\t",l1)
#EXTEND
l1.extend([12,30,40,50,60,70])
print("Extended method\t",l1)
#POP
l1.pop()
print("POP The element at last\t",l1)
#COPY
l1.copy()
print("Copy Method",l1)
#SORT
l1.sort()
#REVERSE
l1.reverse()
print("l1 reverse\t",l1)
