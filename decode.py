# receiver 2nd step
""" 
        DECODING
1. take hex input--> convert binary
2. extract parity bit
3. check parity bit with table
4. check index with the table using binary value
5. output the letter
 """
 #decoding
table1=list("AঅআIইঈUউঊঋEএঐOওঔ")
table2=list("BকখCগঘDঙচFছজGঝঞH") #it's dare darling! bitch
table3=list("টঠJডঢKণতLথদMধনNপ")
table4=list("ফPবভQমযRরলSশষTসহ")
table5=list("Vড়ঢ়Wয়ৎX ্")
table6=list("ঃ ँYা ি ী ")
table7=list(" ু ূ  ৃ ে ৈ ো ৌ")
p=str(int(input("Enter your code: "),16)).rjust(10,'0')          # user input
# decimal & parity difference
decimal=p[4:] 
parity=p[0:4]
binary=int(decimal,2)
if(parity=="0000"):
    print(table1[binary])
if(parity=="0001"):
    print(table2[binary])
if(parity=="0010"):
    print(table3[binary])
if(parity=="0011"):
    print(table4[binary])
if(parity=="0100"):
    print(table5[binary])
if(parity=="0101"):
    print(table6[binary])
if(parity=="0111"):
    print(table7[binary])