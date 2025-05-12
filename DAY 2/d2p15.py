s1={1,3,6,3,8,9,1,9,8,2,32,44}
print(s1)

s1.add(50)
print(s1)
#WE CAN"T FIND ESTIMATE INDEX

#REMOVE() IN SET
s1.remove(8)
print("After remove\t",s1)
#s1.remove(100)#KEYERROR if we dont have that element but we want to remove means it gives"KeyError"
#print("After remove\t",s1)


#DISCARD() IN SET
s1.discard(6)
print("After discard\t",s1)
s1.discard(100)#IT WONT GENERATE ERROR BUT>> IT LEAVE THE STEP AND GENERATE THE PREVIOUS SET
print("After discard\t",s1)


#POP() IN SET--->WE CAN"T ASSIGN THE ELEMENT IN POP METHOD TO POP THE ELEMENT BECAUSE < IT DONT HAVE ANY ORDER> >>POP METHOD
s1.pop()#IT WILL POP FIRST ELEMENT-->Because ,we don't have order in set so, it pop the first element
print("After POP\t",s1)

#COPY() IN SET
s2=s1.copy()
print("COPY \t ",s2)
