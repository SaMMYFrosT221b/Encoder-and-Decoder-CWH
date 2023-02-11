import random
import string

def encoder(s):
    if(len(s)<=3):
        temp = ""
        for i in range(len(s)-1,-1,-1):
            temp = temp +s[i]
        print("Your Encoded string is : "+temp)
    else:
        a=s[0]
        s=s[1:]+a
        string = "abcdefghijklmnopqrstuvwxyz"
        temp =""
        for i in range(0,6):
            r_num = int(random.randrange(0,26,1))
            temp = temp+string[r_num]
        final = temp[0:3]+s+temp[3:]
        print("Your Encoded string is : "+final)

def decoder(s):
    if(len(s)<=3):
        temp = ""
        for i in range(len(s)-1,-1,-1):
            temp = temp +s[i]
        print("Word after decoding: "+temp)
    else:
        a=s[-4]
        s=s[3:len(s)-3]
        s=a+s[0:len(s)-1]
        print("Word after decoding: "+s)

print("What do you want : ")
print("1: Encoidng")
print("2: Decoding")
choice = input()
if(choice=="1"):
    s=input("Enter a string: ")
    encoder(s)
elif(choice=="2"):
    s=input("Enter a string: ")
    decoder(s)
else:
    print("Invalid Input! Please Enter valid input - 1 or 2 ")