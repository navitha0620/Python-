sentence=input("enter any word or sentence:\t")
for ch in sentence:
    ch=ch.lower()
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        print(ch,end=",")