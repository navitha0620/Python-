#FACTORIAL OF A NUMBER USING REDUCE() METHOD
from functools import reduce 
def func(a,b):
    return a*b

#n=int(input("n:\t"))-->Standard input 
r1=range(1,11)#(1,5)-->4=24 {FACTORIAL OF 4}
s=reduce(func,r1)#s=reduce(func,range(1,11))
print(f"result:\t{s}")#GIVES FACTORIAL OF 10=3628800