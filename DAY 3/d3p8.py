#LIST WITHOUT COMPHRENSIONS
#-->>LIST<<--
l1=[1,2,3,4,5]#Sequence object
l2=[]
print("l1:\t",l1)
for ele in l1:
   l2.append(ele**2)
print(f"l2:\t{l2}")

#DICTIONARY WITHOUT COMPHRENSIONS
#-->>DICTIONARY<<--
d1={}
for i in l1:
   d1.update({i:i**2})
print(f"d1:\t{d1}")