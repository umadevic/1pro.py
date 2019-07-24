#a
    
gh=int(input())
ne=list(map(int,input().split()))
ne.sort()
sin=0
see=0
for i in range(len(ne)):
    if ne[i]>=sin:
        see=see+1
    sin=sin+ne[i]
print(see)
