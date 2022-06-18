#receiver 1st step
f1 = open("encoding2.txt", "r")
f2=open("encoding3.txt","a")
data=str(f1.read())
key=list(input("Enter the key: ").split())
key.reverse() #it's dare darling! bitch
count=len(data)
l=list()
for i in key:
    k_index1=data.find(i)
    k_index2=k_index1+len(i)
    l.append(data[k_index2:count])
    count=k_index1
l.reverse()
s=str("\n".join(l))
f2.write(s)