d2={1:"Navitha",
    2:"Navi",
    3:"vitha",
    4:"vitha Navi",
    5:"Navi Vitha",
    6:"Na Vitha",
    #[10,20]:"Heeeeee"---->TypeError : unhashable type :"list"
    (10,20):"Heeeee"#AS a "key"  "IMMUTABLE" objects can be used like "tuple"
}
print(d2)

#get()  METHOD IN DICT-->To find value from the dict --> get (key)
print(  d2.get(1)  )

#keys() Method IN dict -->All keys of the dict
l1=d2.keys()
print("KEYS\t",l1)

#Values() Method IN dict-->All values in the dict	
l2=d2.values()
print("Values\t",l2)

#POP()-->Remove the elementt with specified key-->pop (1)
d2.pop(1)
print("After pop\t",d2)

#POPITEM() Methid IN dict-->Remove last element from dict
d2.popitem()
print("After POPITEM\t",d2)

#UPDATE() Method IN dict-->give like an dict {key:"values"} for update-->IT WILL UPDATE THE LAST ELEMENT 
d2.update({7:"Bandi"})
print("UPDATE\t",d2)

d2.update({2:"Na VI"})
print("UPDATE REPLACE ALREADY WITH THST KEY  \t",d2)

#SETDEFAULT() -->IF THERE IS THAT KEY(WORK LIKE AN SEARCH METHOD) IT RETURNS CORRESPONDING VALUE
value=d2.setdefault(3,"vitha")
print("SETDEFAULT\t",value)

value=d2.setdefault(1,"vitha")# IF THERE IS NO KEY IT ADD KEY_VALUE PAIR AND DISPLAYES THAT VALUE
print("SETDEFAULT\t",value)
print(d2)

#FROMKEYS() -->CREATING NEW DICTIONARY WITH KEYS
stdt=dict.fromkeys(range(1,81))
#print(stdt)
stdt.update({1:(99,100,89,90)})
print("UPDATED STUDENT\t",stdt)

