l1=[1,2,3,5,6,7,4]
print("MInimum:\t",min(l1))
print("Maximum:\t",max(l1))
print("Length:\t",len(l1))
print("Any One element is TRUE:\t",any(l1))#0 & None only be the TRUE
print("Any One element is TRUE:\t",any([None,1,2,3,4,5]))
print("Any One element is TRUE:\t",any([None,0,""]))
print("All TRUE:\t",all(l1)) 
print("All TRUE:\t",all([None,1,2,3,4,5])) 
print("All TRUE:\t",all([None,0,""]))
ch='a'
print(ord(ch))#Unicode Values---> 'a'=97 
l1.sort()


#sorted() PASSING A Tuple
#TUPLE
t1=(10,25,31,78,34)
sl1=sorted(t1)
print("tuple sort\t",sl1)
#SET
sl2={10,25,31,78,34}
sl3=sorted(sl2,reverse=True)
print("Revrese:\t",sl3)
#SET can't be reversable
l1=[1,2,3]
l2=['Navi','Vitha','Navitha']
z=zip(l1,l2)
print(list(z))