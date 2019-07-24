#a
inp=int(input())

ii1=0

ty=0

b=[]

while ii1<90 and ii1<inp:

  s=0

  for j in str(inp-ii1):

    s+=int(j)

  if s+(inp-ii1)==inp:

    ty+=1

    b.append(inp-ii1)

  ii1+=1

print(ty)

for ii in b:

  print(ii1)
