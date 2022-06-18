# sender 1st step 
""" 
        ENCODING
1. user input--> individual capital letter
2. check index with the tables
3. convert to binary
4. parity bit according to tables
5. print hex value
"""
#encoding
import os
import random
table1=list("AঅআIইঈUউঊঋEএঐOওঔ")
table2=list("BকখCগঘDঙচFছজGঝঞH")
table3=list("টঠJডঢKণতLথদMধনNপ")
table4=list("ফPবভQমযRরলSশষTসহ")
table5=list("Vড়ঢ়Wয়ৎX ্")
table6=list("ঃ ँYা ি ী ")
table7=list(" ু ূ  ৃ ে ৈ ো ৌ")
f1 = open("encoding1.txt", "a")
count=0
""" 
1. coverting index of letter to binary
2. adjusting it to make it 4 bits """
def before_parity(p):
    p = bin(p).replace("0b", "")
    p = str(p)
    p=p.rjust(6,'0')
    return p
# user input
msg = list(input("Enter your message: ").upper())
for i in msg:
    for j in table1:
        if i == j:
            p = table1.index(j)
            p=before_parity(p)
            # adding parity
            p = ("0000"+p)
    for j in table2:
        if i == j:
            p = table2.index(j)
            p=before_parity(p)
            # adding parity
            p = ("0001"+p)
    for j in table3:
        if i == j:
            p = table3.index(j)
            p=before_parity(p)
            # adding parity
            p = ("0010"+p)
    for j in table4:
        if i == j:
            p = table4.index(j)
            p=before_parity(p)
            # adding parity
            p = ("0011"+p)
    for j in table5:
        if i == j:
            p = table5.index(j)
            p=before_parity(p)
            # adding parity
            p = ("0100"+p)
    for j in table6:
        if i == j:
            p = table6.index(j)
            p=before_parity(p)
            # adding parity
            p = ("0101"+p)
    for j in table7:
        if i == j:
            p = table7.index(j)
            p=before_parity(p)
            # adding parity
            p = ("0111"+p)
    p = int(p)
    new_code=(hex(p)[2:])
    f1.write(new_code+"\n") #it's dare darling! bitch
    count+=1
f1.close()
# sender 2nd step
# steganography starting
def specific_string(length):  
    sample_string = '1234567890abcdef' # define the specific string  
    # define the condition for random string  
    result = ''.join((random.choice(sample_string)) for x in range(length))  
    return result
f2 = open("encoding1.txt", "r")
f3 = open("encoding2.txt", "a")
key=[]
for i in f2:
    a=random.randint(1,50)
    g=specific_string(a)
    f3.write(g)
    f3.write(i.rstrip())
    key.append(g)
f2.close()
f3.close()
os.remove("encoding1.txt")
print(' '.join(key))