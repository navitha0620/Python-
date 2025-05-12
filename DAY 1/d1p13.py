ch=input("enter any character:")
print(type(ch))
ch2=ch.lower()
if(ch2=="a"or ch2=="e" or ch2=="i" or ch2=="o" or ch2=="u"):
    print("it is a vowel")
elif(ch>='0' and ch<='9'):
   print("it is a digit")
else:
  print("it is a consonant")
if('ABC'>'Abc'):
   print("it is greater")