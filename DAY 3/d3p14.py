#reduce()-->Working to reduce
#

from functools import reduce 
def func(a,b):
    return a+b

r1=range(1,11)
s=reduce(func,r1)
#IT TAKES 1,2 values for first iteration tkaes by reduce and holds it then taken 3 as next value ....Sends to fnc then returns final value
print(f"result:\t{s}")
