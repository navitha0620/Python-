s1={10,10,20,40,90}
s2={10,90,14,50,30}

#INTERSECTION_UPDATE() IN SET
s1.intersection_update(s2)
print("Intersection_Update\t",s1)

#INTERSECTION() IN SET
s4=s1.intersection(s2)
print("Intersection\t",s4)

#DIFFERENCE() IN SET 
s1.difference(s2)
print("Difference s1\t",s1)
print("s1\t",s1)

#UNION() IN SET
s=s1.union(s2)
print("UNION s: \t",s)
print("s1\t",s1)
print("s2\t",s2)

#UPDATE() IN SET or UPDATE UNION () IN SET
s1.update(s2)
print("Update Union s:\t",s1)

#DIFFERNCE_UPDATE() IN SET
s1.difference_update(s2)
print("Difference_Update\t",s1)


#SYMMETRIC_DIFFERENCE() IN SET
s6=s1.symmetric_difference(s2)
print("Symmetric\t",s6)

#SYMMETRIC_DIFFRENCE_UPDATE() IN SET
s1.symmetric_difference_update(s2)
print("Symmetric\t",s1)

