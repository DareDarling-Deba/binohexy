from tkinter import *
window=Tk()
def fun():
    table1=list("AঅআIইঈUউঊঋEএঐOওঔ")
    table2=list("BকখCগঘDঙচFছজGঝঞH") #it's dare darling! bitch
    table3=list("টঠJডঢKণতLথদMধনNপ")
    table4=list("ফPবভQমযRরলSশষTসহ")
    table5=list("Vড়ঢ়Wয়ৎX ্")
    table6=list("ঃ ँYা ি ী ")
    table7=list(" ু ূ  ৃ ে ৈ ো ৌ")
    code=list(cover.get().split())
    for i in code: 
        p=str(int(i,16)).rjust(10,'0')          # user input
# decimal & parity difference
        decimal=p[4:] 
        parity=p[0:4]
        binary=int(decimal,2)
        if(parity=="0000"): 
            l2.insert(END,table1[binary])
        if(parity=="0001"): 
            l2.insert(END,table2[binary])
        if(parity=="0010"): 
            l2.insert(END,table3[binary])
        if(parity=="0011"):
            l2.insert(END,table4[binary])
        if(parity=="0100"):
            l2.insert(END,table5[binary])
        if(parity=="0101"):
            l2.insert(END,table6[binary])
        if(parity=="0111"):
            l2.insert(END,table7[binary])
pu1=Label(window,text="Please enter cover text :").pack()
cover= Entry(window)
cover.pack()
submit= Button(window, text="Submit",command=fun)
submit.pack()
l2= Text(window, height=1, borderwidth=0)
l2.pack()
window.mainloop()