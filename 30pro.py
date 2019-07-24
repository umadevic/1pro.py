#a

n9=input()
ca1=0
for i in range(0,len(n9)):
    ss1=n1[0:i]+n1[i+1::]
    if int(ss1)%8==0:
        ca1=1
        break
if ca1==1:
    print("yes")
else:
    print("no")
