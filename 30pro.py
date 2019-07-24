#a

n9=input()
cb=0
for i in range(0,len(n9)):
    ss=n9[0:i]+n9[i+1::]
    if int(ss)%8==0:
        cb=1
        break
if cb==1:
    print("yes")
else:
    print("no")
