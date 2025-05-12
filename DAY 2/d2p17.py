#SET OBJECT METHODS()

#isdisjoint()--> TWO SETS ARE TO BE DIFFERENT
s1={10,10,20,40,90}
s2={1,2,3,4}

f=s1.isdisjoint(s2)
print("ISDISJOINT\t",f)


s1=set(range(1,11))#Here we are creating constructor(1,11) to an "range" class-->Passing range object to the set class constructor
#s1=set(1,2,3,4,5,6,7,8,9,10)
print(s1)

#ANOTHER METHOD FOR PASSING ELEMENTS TO THE SET
s2=set([12,3,45,3])
print(s2)

#ISSUBSET()
f1=s1.issubset(s2)
print("ISSUBSET\t",f1)


#ISSUPERSET()
f2=s1.issuperset(s2)
print("ISSUPERSET\t",f2)
