from tkinter import Button, Label, Tk
from tkinter.ttk import Entry
window = Tk()
window.title("Information finding")
def fun():
    # receiver 1st step
    f1 = open("encoding2.txt", "r")
    f2 = open("encoding3.txt", "w")
    data = str(f1.read())
    key = list(key1.get().split())
    key.reverse()  # it's dare darling! bitch
    count = len(data)
    l = list()
    for i in key:
        k_index1 = data.find(i)
        k_index2 = k_index1+len(i)
        l.append(data[k_index2:count])
        count = k_index1
    l.reverse()
    s = str(" ".join(l))
    f2.write(s)
pu1 = Label(text="Enter your key: ")
pu1.pack()
key1 = Entry(window)
key1.pack()
b1 = Button(window, text="Submit", command=fun)
b1.pack()

window.mainloop()
