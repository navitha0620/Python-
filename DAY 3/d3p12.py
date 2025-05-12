def func(i):
    return i%2==0 #TRUE OR FALSE
r1=range(1,11)#sequence object
m=map(func,r1)#TRUE OR FALSE
#RETURNED VALUE CAN BE GET 
print("First Time")
for ele in m:
    print(ele)