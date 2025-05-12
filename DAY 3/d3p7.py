#USING COMPHRENSIONS 
#LIST,TUPLE,DICTIONARY,GENERATORS(SETS)

l1=[1,2,3,4,5] #Sequence-object#LIST
l2=[i*i for i in l1 ] #list comphrensions [] ----> loop 1: i=1 >>> i*i=1*1=1

#TUPLE
l3={i*i for i in l1}
print("l3:\t",l3)

#SETS
g1=(i*i for i in l1)
print("g1:\t",g1)
for ele in g1:
    print(ele)
print("l1:\t",l1)
print("l2:\t",l2)

#DICTIONARY
l3=[1,2,3,4,5] #Sequence-object
d2={i:i*i for i in l1 }
print("d2:\t",d2)

