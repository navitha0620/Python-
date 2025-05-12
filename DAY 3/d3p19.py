#Write a program to check whether a given sentence is Pangram or not..?
#Sentence==>"The quick brown fox jumps over the lazy dog"


#METHOD-1
import string
def pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    letters = set(sentence.lower())
    return alphabet <= letters
test = "The quick brown fox jumps over the lazy dog"
if pangram(test):
    print("Yes Pangram...!")
else:
    print("Not Pangram.")

#METHOD-2
s2="Hello"
alphabets="abcdefghijklmnopqrstuvwxyz"
flag=True
for ch in alphabets:
    if ch not in s2:
        flag=False
        break #Comes out of the for loop not from the if loop 
if flag==True:
    print("Is Pangram")
else:
    print("Is Pangram")


#METHOD-3
s1="The quick brown fox jumps over the lazy dog"
alphabets="abcdefghijklmnopqrstuvwxyz"
flag=True
for ch in alphabets:
    if ch not in s1.lower():
        flag=False
        break
if flag:
    print("True Pangram")
else:
    print("False Pangram")
