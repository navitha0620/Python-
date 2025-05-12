a=0
b=0
c=0
try:#Chance of getting errors
    a=int(input("a:\t"))
    b=int(input("b:\t"))
    c=a/b
except ValueError as error:#Errors to handle
    print(error)
except ZeroDivisionError as error:
    print(error)
finally:
    print("Okay Finally..!")
print(f"{a}/{b}={c}")
